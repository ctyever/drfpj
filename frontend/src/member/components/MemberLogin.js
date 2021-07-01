import React, {useState} from 'react'
import { memberLogin } from 'api/index'
// import './Login.css'
const MemberLogin = () => {

    const [userInfo, setUserLogin] = useState({
      username : '',
      password : ''
    })

    const {username, password} = userInfo

    const handleSubmit = e => {
      e.preventDefault()
      memberLogin({...userInfo})
      .then(res => {
        alert(`로그인 성공 : : ${res.data.result}`)
      })
      .catch(err => {
        alert(`로그인 실패 : ${err}`)
      })
    }

    const handleClick = e => {
      e.preventDefault()
    }

    const handleChange = e => {
      const {name, value} = e.target
      e.preventDefault()      
      setUserLogin({
        ...userInfo, 
        [name]: value
      }
      )

    }

    return (<>
    <h2>Login Form</h2>

<form method="post" onSubmit={handleSubmit}>
  <div className="imgcontainer">
    <img src="https://www.w3schools.com/howto/img_avatar2.png" style={{width: "300px"}} alt="Avatar" className="avatar"/>
  </div>

  <div className="container">
    <label labelFor="username"><b>Username</b></label>
    <input type="text" onChange={handleChange} placeholder="Enter Username" name="username" value={username} required/>

    <label labelFor="password"><b>Password</b></label>
    <input type="password" onChange={handleChange} placeholder="Enter Password" name="password" value={password} required/>
        
    <button type="submit">Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"/> Remember me
    </label>
  </div>

  <div className="container" style={{backgroundColor: "#f1f1f1"}}>
    <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
    <span className="psw">Forgot <a href="#">password?</a></span>
  </div>
</form>
   
    </>)
}

export default MemberLogin