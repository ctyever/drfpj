import React, { useState } from 'react'
import { useHistory } from 'react-router'
import { userPostup } from 'api/index'

const PostWrite = () => {


    const [userPost, setUserPost] = useState({
      title: '',
      content: ''
    })

    const {title, content} = userPost

    const handleSubmit = e => {
      e.preventDefault()
      userPostup({...userPost})
      .then(res => {
        alert(`게시글 쓰기 완료 : ${res.data.result}`)
      })
      .catch(err => {
        alert(`회원가입 실패 : ${err}`)
      })            
    }

    const handleClick = e => {
      e.preventDefault()
    }

    const handleChange = e => {
      const { name, value } = e.target
      e.preventDefault()
      setUserPost({
        ...userPost, 
        [name]: value
      })
    }

    
    
    return (<>
    <div className="PostWrite">
    <form onSubmit={handleSubmit} method='post' style={{border:"1px solid #ccc"}}>
  <div className="container">
    <h1>게시글 쓰기</h1>
    
    <hr/>

    <label for="title"><b>Title</b></label>
    <input type="text" placeholder="Enter Title" onChange={handleChange} name="title" value={title}/>

    <label for="content"><b>Content</b></label>
    <input type="text" placeholder="Enter Content" onChange={handleChange} name="content" value={content}/>

    <div class="clearfix">
      <button type="submit" className="signupbtn">Sign Up</button>
      <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
     
    </div>
  </div>
</form>
</div>
</>)
}

export default PostWrite