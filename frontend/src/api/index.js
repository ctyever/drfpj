import axios from 'axios'

const server = 'http://127.0.0.1:8000/'

export const userSignup = signupRequest => axios.get(`${server}member/signup`, signupRequest)
export const userLogin = loginRequest => axios.post(`${server}member/login`, loginRequest)
