import React,{ useState } from 'react'
import { memberDelete } from 'api/index'
import { useHistory } from 'react-router'
const MemberDeleteForm = () => {
    const [password, setPassword] = useState({})

    const history = useHistory()

    const handleSubmit = e => {
      e.preventDefault()
      const member = JSON.parse(localStorage.getItem("loginedMember"))      
      member.password = password
     

      memberDelete({member})
      .then(res => {
        if(res.data.result === 'PASSWORD-FAIL'){
          alert('비밀번호가 틀립니다')  
        }else{
        alert(`탈퇴 완료 : ${res.data.result} `)
        localStorage.setItem("loginedMember","")
        history.push('./home')
        }
      })
      .catch(err => {
        alert(`탈퇴 실패 : ${err} `)
  
      })
    }


    return (<>
      <form method="put" onSubmit={handleSubmit} >
            
                <h2 style={{"text-align":"center"}}>회원탈퇴</h2>
        <div className="container">
          <label labelFor="password"><b>비밀번호 </b></label>
          <input type="password" placeholder="Enter Password" onChange={e => {setPassword(e.target.value)}} name="password" required/>
              
          <button type="submit">확 인</button>
         
        </div>

      </form>
 
      </>)
}

export default MemberDeleteForm