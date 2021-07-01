import React, {useEffect, useState} from 'react'
import axios from 'axios';
import { Button } from '@material-ui/core';


const Home = ({children}) => {

    const [connection, setConnection ] = useState(false)
    /* 
    useEffect(()=>{
        
    },[])
    */
    const handleClick = e => {
        e.preventDefault()
        axios({
            method: "get",
            url: "http://127.0.0.1:8000/connection",
            responseType: "json"
        }).then(function (res) {
            setConnection(res.data.connection === 'success')
        });        
    }
    
    return (<>
    <table className="tab_lay">
        
        <tr><td><Button color="primary" onClick={handleClick}>서버 연결 테스트</Button></td></tr>
        <tr><td>{ connection ? 
        '연결상태 입니다'
        : 
        '연결상태가 아닙니다'
        }</td></tr>
    </table>
    {children}

</>)}


export default Home




