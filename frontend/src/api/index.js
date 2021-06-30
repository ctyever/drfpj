import axios from 'axios'

const SERVER = 'http://127.0.0.1:8000/'
const headers = {'Content-Type': 'application/json'}
// const headers_xml = {'Content-Type': 'application/xml'}

export const userSignup = body => axios.post(`${SERVER}member/signup`, {headers, body})
export const userLogin = body => axios.post(`${SERVER}member/login`, {headers, body})
// export const userLogin = body => axios.post(`${SERVER}member/login`, {headers: headers_xml, body})
export const userPostup = body => axios.post(`${SERVER}board/postup`, {headers, body})
