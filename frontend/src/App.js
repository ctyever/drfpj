import React from 'react'
import { Redirect, Route } from "react-router-dom"
import { Login, Signup, UserDetail, UserEdit, UserList  } from 'user'
import { PostWrite } from 'board'
import { Home, User, Blog, Item, Stock} from 'templates'
import { Nav } from 'common'
import { BrowserRouter as Router } from 'react-router-dom'
import { Link } from 'react-router-dom'

const App = () => {
  return (<div>
    <Router>
        <Nav/>  
        <Route exact path='/home' component={Home}/>
        <Redirect exact from={'/'} to={'/home'}/>
        <Route exact path='/user' component={User}/>
        <Route exact path='/login' component={Login}/>
        <Route exact path='/signup' component={Signup}/>
        <Route exact path='/user-detail' component={UserDetail}/>
        <Route exact path='/user-edit' component={UserEdit}/>
        <Route exact path='/user-list' component={UserList}/>
        <Route exact path='/item' component={Item}/>
        <Route exact path='/blog' component={Blog}/>
        <Route exact path='/postlist' component={PostWrite}/>
        <Route exact path='/postup' component={PostWrite}/> 
        <Route exact path='/postretreive' component={PostWrite}/> 
        <Route exact path='/postdetail' component={PostWrite}/> 
        <Route exact path='/postupdate' component={PostWrite}/>
        <Route exact path='/postdelete' component={PostWrite}/>          
        <Route exact path='/stock' component={Stock}/>
    </Router>
  </div>)
}

export default App