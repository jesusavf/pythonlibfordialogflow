from flask import Flask, request, make_response, jsonify
import random
def msj(text):
     return '{"fulfillmentText": "'+text+'", "fulfillmentMessages": [ { "text": { "text": [ "'+text+'" ] } } ]}'
def rndmsj(textx):
    text=random.choice(textx)
    return '{"fulfillmentText": "'+text+'", "fulfillmentMessages": [ { "text": { "text": [ "'+text+'" ] } } ]}'
def credenciales(user,passw,vuno,vdos):
    if user==vuno:
        if passw==vdos:
            return True
        else:
            exit()
    else:
        exit()
def instancia(nombre):
    req = request.get_json(force=True)
    if req.get('queryResult').get('intent').get('displayName')==nombre:
        return True
    else:
        return False

def variable(nombre):
    req = request.get_json(force=True)
    if req.get('queryResult').get('parameters').get(nombre):
        return req.get('queryResult').get('parameters').get(nombre)
    else:
        return ''
def origenes():
    req = request.get_json(force=True)
    if req.get("originalDetectIntentRequest").get("payload").get("source"):
        return (req.get("originalDetectIntentRequest").get("payload").get("source").upper())
    else:
        frase = u'indefinido'
        return frase.upper()
def texto():
    req = request.get_json(force=True)
    if req.get("queryResult").get("queryText"):
        return req.get("queryResult").get("queryText")
    else:
        return ''
def imagen():
    req = request.get_json(force=True)
    if req.get("originalDetectIntentRequest").get("payload").get("data").get("message").get("attachments").get(0).get("payload").get("url"):
        return req.get("originalDetectIntentRequest").get("payload").get("data").get("message").get("attachments").get(0).get("payload").get("url")
    else:
        return ''
    
def enviarimagenes(imagen,plataforma):
    a='{"fulfillmentMessages":['
    for img in imagen:
        a=a+'{"image":{"imageUri":"'+img+'"},"platform":"'+plataforma+'"},'
    a=a+'{"payload":{}}]}'
    return a
def enviartarjetas(t,plataforma):
    a='{"fulfillmentMessages": ['
    con=1
    for tit in t:
        try:
            a=a+'{"card": {"title": "'+tit[1]+'", "subtitle": "'+tit[2]+'", "imageUri": "'+tit[3]+'"'
            a=a+', "buttons": [ { "text": "'+tit[0][0]+'"} '
            con=2
            a=a+', { "text": "'+tit[0][1]+'"} '
            a=a+', { "text": "'+tit[0][1]+'"} '
            a=a+']}, "platform": "'+plataforma+'"},'
        except IndexError:
            if con==1:
                a=a+'}, "platform": "'+plataforma+'"},'
            else:
                a=a+']}, "platform": "'+plataforma+'"},'
    a=a+'{"payload":{}}]}'
    return a
def enviarrespuestasrapidas(repuestas,plataforma):
    a='{ "fulfillmentMessages": [ { "quickReplies": { "title": "'+repuestas['titulo'][0]+'",  "quickReplies": ['
    b=repuestas['boton']
    d=''
    for c in b:
        if d=='':
            d=d+'"'+c+'"'
        else:
            d=d+',"'+c+'"'
    a=a+d+']},"platform": "'+plataforma+'"},{"payload":{}}]}'
    return a
  
