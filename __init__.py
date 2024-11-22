
import configparser
import json
import platform
import requests
import traceback
import os

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'Xperience' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from configurationObject import ConfigObject
from orchestator import OrchestatorCommon

global configFormObject
global path_ini_assetnoc_
global verify_form

module = GetParams('module')

if module == 'Login':
    server_ = GetParams("server_url")
    var_ = GetParams('var_')
    iframe = GetParams("iframe")
    iframe = eval(iframe) if iframe is not None else {}
    username = iframe.get("user", "")
    password = iframe.get("password", "")
    api_key = iframe.get("apikey", "")
    path = iframe.get("path_ini", GetParams("ruta_"))
    path_ini_assetnoc_ = path
    proxies = GetParams("proxies")
    user_proxies = GetParams("user_proxies")
    pass_proxies = GetParams("pass_proxies")
    verify_ = GetParams("verify")

    try:
        if not proxies:
            proxies = None
        
        if verify_ and eval(verify_):
            verify_form = False
        else:
            verify_form = True

        if user_proxies and pass_proxies:
            user_proxies = urllib.parse.quote(f"{user_proxies}")
            pass_proxies = urllib.parse.quote(f"{pass_proxies}")
            protocolo = proxies.split('://')[0] + "://"
            server = proxies.split('://')[1]
            url_proxy = protocolo + user_proxies + ":" + pass_proxies + "@" + server
            proxies = {"http": url_proxy, "https": url_proxy}
            print(proxies)

        if password and username:
            try:
                orchestrator_service = OrchestatorCommon(server=server_, user=username, password=password, ini_path=path, apikey=api_key)
                if server_ is None:
                        server_ = orchestrator_service.server
                token = orchestrator_service.get_authorization_token()
                headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
                res = requests.post(server_ + '/api/formData/all',
                                    headers=headers, proxies=proxies, verify=verify_form)
                configFormObject = ConfigObject(token, orchestrator_service.server, orchestrator_service.user, orchestrator_service.password, api_key, proxies=proxies)
                conx = True
                SetVar(var_, conx) #type: ignore

            except:
                if res.status_code != 200:
                    exc = res.json()['message'] if res.json()['message'] else "Password o E-mail incorrectos"
                    raise Exception(exc)
                raise Exception("Password o E-mail incorrectos")

        elif api_key:
                 
            orchestrator_service = OrchestatorCommon(server=server_, user=username, password=password, ini_path=path, apikey=api_key)
            if server_ is None:
                server_ = orchestrator_service.server
            token = orchestrator_service.get_authorization_token()
            headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
            res = requests.post(server_ + '/api/formData/all',
                                headers=headers, proxies=proxies, verify=verify_form)
            configFormObject = ConfigObject(token, orchestrator_service.server, orchestrator_service.user, orchestrator_service.password, api_key, proxies=proxies)
            if res.status_code != 200:
                exc = res.json()['message'] if res.json()['message'] else "El API Key es incorrecto"
                raise Exception(exc)
            else:
                conx = True
            SetVar(var_, conx)

        elif path:
            try:
                orchestrator_service = OrchestatorCommon(server=server_, user=username, password=password, ini_path=path, apikey=api_key)
                if server_ is None:
                    server_ = orchestrator_service.server
                token = orchestrator_service.get_authorization_token()
                headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
                res = requests.post(server_ + '/api/formData/all',
                                    headers=headers, proxies=proxies, verify=verify_form)
                configFormObject = ConfigObject(token, orchestrator_service.server, orchestrator_service.user, orchestrator_service.password, api_key, proxies=proxies)
                conx = True
                SetVar(var_, conx)
            except:
                if res.status_code != 200:
                    exc = res.json()['message'] if res.json()['message'] else "Password o E-mail incorrectos"
                    raise Exception(exc)
                raise Exception("Password o E-mail incorrectos")
    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e
    
if module == 'GetForm':
    token_ = GetParams('token')
    var_ = GetParams('result')

    try:
        res = requests.post(configFormObject.server_ + '/api/formData/get/' + token_,
                            headers={'Authorization': "Bearer " + configFormObject.token}, proxies=configFormObject.proxies, verify=verify_form)
        if res.status_code == 200:
            tmp = []
            res = res.json()
            if 'data' in res:
                for data in res['data']:
                    aa = {'id': data['id']}
                    tmp.append(aa)
            SetVar(var_, tmp)
        else:
            raise Exception(res.json())

    except Exception as e:
        PrintException()
        # print(res.json())
        raise e

if module == 'GetFormData':
    id_ = GetParams('id_')
    token_ = GetParams('token_')
    result = GetParams('result')
    set_ = GetParams('set_var_name')

    try:
        if set_:
            set_ = eval(set_)

        res = requests.post(configFormObject.server_ + '/api/formData/getQueue/' + id_ + '/' + token_,
                            headers={'Authorization': "Bearer " + configFormObject.token}, proxies=configFormObject.proxies, verify=verify_form)
        if res.status_code == 200:
            result_dict = {}
            res = res.json()

            if 'data' in res:

                data = json.loads(res['data']['data'])
                if isinstance(data, dict):
                    for attr, value in data.items():
                        if attr == 'file':
                            value = value.split("/")[-1]
                        result_dict[attr] = value
                        if set_:
                            SetVar(attr, value)
                else:
                    result_dict = data

                    

            if 'user_form_email' in res['data']:
                SetVar('user_form_email', res['data']['user_form_email'])

            if 'xperience' in res['data']:
                SetVar('xperience', res['data']['xperience'])

            SetVar(result, result_dict)

        else:
            raise Exception(res.json()['message'])

    except Exception as e:
        PrintException()
        raise e

if module == 'SetStatus':
    status_ = GetParams('status_')
    id_ = GetParams('id_')
    _var = GetParams('result_')

    if not id_:
        raise Exception("No form data loaded")
    try:
        s = 0
        lock = 0
        if status_ == 'done':
            s = 1
        elif status_ == 'undone':
            s = 0

        if status_ == 'lock':
            lock = 1
        data = {'status': s, 'locked': lock}
        res = requests.post(configFormObject.server_ + '/api/formData/setStatus/' + str(id_), data=data,
                            headers={'Authorization': "Bearer " + configFormObject.token}, proxies=configFormObject.proxies, verify=verify_form)

        res = res.json()
        if _var:
            SetVar(_var, res['success'])
        if not res['success']:
            raise Exception(res['message'])
    except Exception as e:
        PrintException()
        raise e

if module == "DownloadFile":
    id_ = GetParams('id_')
    download_ = GetParams('download_')
    save_ = GetParams('save_')

    try:
        if not id_:
            raise Exception("No queue ID provided")
        if not download_:
            raise Exception("No file to download provided")
        if not save_:
            raise Exception("No path to save file provided")

        data = {'file': download_}
        
        if "/" in download_:
            filename = download_.split("/")[-1]
        if download_ in save_:
            save_ = save_.replace(download_, filename)
        
        myDirs = save_.split("/")[:-1]
        if (platform.system() == 'Windows'):
            myDirs[0] = myDirs[0] + "\\"
        myDirs = os.path.join(*myDirs)

        os.makedirs(myDirs, exist_ok=True)

        res = requests.post(configFormObject.server_ + '/api/formData/download/' + str(id_), data=data,
                            headers={'Authorization': "Bearer " + configFormObject.token}, proxies=configFormObject.proxies, verify=verify_form)
        if res.status_code == 200:
            with open(save_, 'wb') as ff:
                ff.write(res.content)
        else:
            raise Exception("Error ocurred while download file")
    except Exception as e:
        PrintException()
        raise e

if module == "setXperience":

    try:
        xperience = GetParams('xperience')
        extradata = GetParams('extradata')

        data = {'xperience': xperience, 'data': extradata}

        res = requests.post(configFormObject.server_ + '/api/form/extra', data=data,
                            headers={'Authorization': "Bearer " + configFormObject.token}, proxies=configFormObject.proxies, verify=verify_form)

        if res.status_code != 200:
            raise Exception('An error has occurred')

    except Exception as e:
        PrintException()
        raise e

if module == "SendFile":
    path = GetParams('path')
    xperience = GetParams('xperience')
    res = GetParams('res')

    try:
        if not path:
            raise Exception("No file to upload provided")
        
        data = {"xperience": xperience}

        with open (path, 'rb') as file:
            files = {'document': file}

            r = requests.post(configFormObject.server_ + '/api/form/extraFile', files=files,
                            headers={'Authorization': "Bearer " + configFormObject.token}, data=data,
                            proxies=configFormObject.proxies, verify=verify_form)
            
            r = r.json()

            if not r.get('success'):
                raise Exception(r.get('message', ''))
            
            token = r.get('data')

            SetVar(res, token)

    except Exception as e:
        PrintException()
        SetVar(res, False)
        raise e
    
if module == "SearchInForm":
    token_ = GetParams('token_')
    data_name = GetParams('data_name')
    search_value = GetParams('search_value')
    result = GetParams('result')
    autocomplete = eval(GetParams('autocomplete')) if GetParams('autocomplete') else False
    lock_form = eval(GetParams('lock_form')) if GetParams('lock_form') else False
    result_id = GetParams('result_id')


    try:
        result_dict = {}
        res = requests.post(configFormObject.server_ + '/api/formData/get/' + token_,
                            headers={'Authorization': "Bearer " + configFormObject.token}, proxies=None, verify=verify_form)
        if res.status_code == 200:
            tmp = []
            res = res.json()
            if 'data' in res:
                break_ = False
                for data in res['data']:

                    aa = {'id': data['id']}
                    tmp.append(aa)
                    # print("data", data['id'])
                    form_data = requests.post(configFormObject.server_ + '/api/formData/getQueue/' + str(data['id']) + '/' + token_,
                                              headers={'Authorization': "Bearer " + configFormObject.token}, proxies=configFormObject.proxies, verify=verify_form)
                    
                    form_data = form_data.json()
                    
                    if 'data' in form_data:
                        form_data_ = json.loads(form_data['data']['data'])
                        for key, value in form_data_.items():
                            if key == data_name and value == search_value:
                                result_dict = form_data_
                                # print("key", key, "value", value)
                                break_ = True

                                if autocomplete:
                                    for attr, value in form_data_.items():
                                        SetVar(attr, value)
                                if lock_form:
                                    data_lock = {'status': 0, 'locked': 1}
                                    res = requests.post(configFormObject.server_ + '/api/formData/setStatus/' + str(data['id']), data=data_lock,
                                                        headers={'Authorization': "Bearer " + configFormObject.token}, proxies=configFormObject.proxies, verify=verify_form)
                                break

                    if break_:
                        SetVar(result_id, data['id'])
                        SetVar(result, result_dict)
                        break
                    # for key, value in form_data['data']['data'].items():
                    #     if key == data_name and value == search_value:
                            
                    #         break

        else:
            SetVar(result, False)
            raise Exception(res.json())
            
    except Exception as e:
        SetVar(result, False)
        PrintException()
        print(res.json())        
        raise e




if module == 'GetQueuesLocked':
    token_ = GetParams('token')
    var_ = GetParams('result')

    if not token_:
        raise Exception("No token provided")
    try:
        res = requests.post(configFormObject.server_ + '/api/formData/all',
                            headers={'Authorization': "Bearer " + configFormObject.token}, proxies=configFormObject.proxies, verify=verify_form)
        
        if res.status_code == 200:
            tmp = []
            res = res.json()
            queues = []
            if 'data' in res:
                for data in res['data']:
                    if data['locked'] == 1 and data['form_token'] == token_:
                        aa = {'id': data['id']}
                        tmp.append(aa)
            SetVar(var_, tmp)

        else:
            raise Exception("Bad Request, status_code: "+str(res.status_code))

    except Exception as e:
        PrintException()
        raise e

if module == 'GetAllQueues':
    var_ = GetParams('result')
    from_ = GetParams('from_')
    to_ = GetParams('to_')

    try:
        data = {"from": from_, "to": to_}
        queue_res = requests.post(configFormObject.server_ + '/api/formData/all', data=data,
                                headers={'Authorization': "Bearer " + configFormObject.token}, proxies=configFormObject.proxies, verify=verify_form)
        print(queue_res.status_code)
        if queue_res.status_code == 200:
            if isinstance(queue_res, requests.models.Response):
                queue_res = queue_res.json()
            SetVar(var_, queue_res['data'])
        else:
            raise Exception(queue_res['message'])
        
    except Exception as e:
        PrintException()
        raise e