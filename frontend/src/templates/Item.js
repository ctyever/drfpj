import React from 'react'
import { ItemMenu as Menu } from 'common/components/Menu'

const Item = ({children}) => (<>
    <h1>Item</h1>
    <Menu/>
    {children}
</>)

export default Item