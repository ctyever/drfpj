import React from 'react'
import { BlogMenu as Menu } from 'common/Menu'

const Blog = ({children}) => (<>
    <h1>Blog</h1>
    <Menu/>
    {children}
</>)

export default Blog

