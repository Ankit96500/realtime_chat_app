



const GroupName=JSON.parse(document.getElementById('group-name').textContent)

console.log('inside the group name----->',GroupName)
console.log('type of  groupname--',typeof(GroupName))

class WebSockets{    
    constructor(GroupName){
       const ws = new WebSocket('ws://'
        + window.location.host
        + '/webs/sync/'
        + GroupName
        +'/'  
        )
        this.ws = ws;
        console.log('connection opennnn')
        console.log('----',this.ws)
    }

    return_var(){
        return this.ws;
    }
    
}

let WebSockets_obj= new WebSockets(GroupName);

const ws = WebSockets_obj.return_var();
// document.write('wss  object-->',ws)

document.getElementById('disconnect-button').onclick = function(event){
    ws.close();
    console.log('connection band ho gyaya hai..')
}        

document.getElementById('chat-message-submit').onclick = function(event){
        if(ws.readyState == 0 || ws.readyState == 1){

        console.log('inside the event',event)
        const messageinputdom = document.getElementById('chat-message-input')

        const message = messageinputdom.value
        console.log('inside the message---->',message)
        console.log('type of message---->',typeof(message))

        ws.send(JSON.stringify({
            'msg':message
        })); 

        messageinputdom.value = ''
    }                
    
}
console.log(ws.readyState,'<--ready state')


    ws.onmessage = function(event){
        console.log('message server se ayay hai--->',event)
        console.log('message server ka type.....',typeof(event.data))
        // if (event) {
        //     const mata = JSON.parse(event.data)

        //     console.log('inside the query selector inside the if caluse-->',document.querySelector('#chat-log').value += (data.msg + '\n'))
            
        // } 
        const data = JSON.parse(event.data)
        console.log('parsed data ka type',typeof(data))
        console.log('actual message data...',event.data)
        console.log('actual message...',data.msg)
       // document.querySelector('#chat-log').value += (data.msg + '\n')
        console.log('inside the query selector-->',document.querySelector('#chat-log').value += (data.user +': ' +  data.msg  + '\n \n'))
        
    }    

document.getElementById('disconnect-button').onclick()=function () {
    document.write('you are disconnected..')        
}
