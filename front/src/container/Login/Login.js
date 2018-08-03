import React from 'react';
import {leftLogo} from '../../assets/index';
import './Login.css';

export default class Login extends React.Component{
  constructor(){
    super();
    this.state={
      id: '',
      pw: ''
    }
  }
  render(){
    return (
      <div className="Login">
        <div className="Login__Square1"></div>
        <div className="Login__Square2"></div>
        <img src={leftLogo} alt="Entry 3.0 InterView Logo" className="Login__img"/>
        <div className="Login__contents">
          <div className="Login__contents__title">
            <span>Login</span> 
          </div>
            <input type="text" className="Login__contents__input" placeholder="아이디" value={this.state.id} onChange={(event)=>this.setState({id: event.target.value})}/>
            <input type="password" className="Login__contents__input" placeholder="비밀번호" value={this.state.pw} onChange={(event)=>this.setState({pw: event.target.value})}/>
            <button className="Login__contents__btn">로그인</button>
        </div>
      </div>
    )
  }
  getToken(){
    
  }
}