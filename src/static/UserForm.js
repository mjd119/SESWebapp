//import React, { Component } from 'react';
// See https://www.youtube.com/watch?v=x9UEDRbLhJE for class setup
class UserForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            first_name: '',
            last_name: '',
            sex: '',
            birthday: ''
        }
    }
    changeHandler = e => {
        this.setState({[e.target.name]: e.target.value});
    }
    // Couldn't figure out how to make this submit handler work
    submitHandler = e => {
        e.preventDefault();
        console.log(this.state);
        alert(this.state.username);
        let data = JSON.stringify({
            username: this.state.username,
            first_name: this.state.first_name,
            last_name: this.state.last_name,
            sex: this.state.sex,
            birthday: this.state.birthday
        });
        console.log(data);
        axios.post('http://127.0.0.1:5001/', data, {crossDomain: true},
        {
            headers: {
                "Content-Type": "text/enriched",
                "Access-Control-Allow-Origin": "/",
                "Referrer-Policy": "origin-when-cross-origin"
            }
        })
        .then((response) => {
            console.log("No error");
            console.log(response);
        })
        .catch((error) => {
            console.log("This is is an error!");
            console.log(error.response.data);
        })
    }
    render() {
        const { username, first_name, last_name, sex, birthday } = this.state;
        return (
          <div>
                <form method="post" action="/hello">
                  <div>
                    <input id="username" type="text" name="username" placeholder="Enter username" required value={username} onChange={this.changeHandler}></input>
                  </div>
                  <div>
                    <input id="first_name" type="text" name="first_name" placeholder="Enter first name" required value={first_name} onChange={this.changeHandler}></input>
                  </div>
                  <div>
                    <input id="last_name" type="text" name="last_name" placeholder="Enter last name" required value={last_name} onChange={this.changeHandler}></input>
                  </div>
                  <div>
                    <select id="sex" name="sex" value={sex} required onChange={this.changeHandler}>
                      <option value="" defaultValue disabled hidden>Sex</option>
                      <option value="F">Female</option>
                      <option value="M">Male</option>
                    </select>
                  </div>
                  <div>
                    <input id="birthday" type="date" name="birthday" value={birthday} required onChange={this.changeHandler}></input>
                  </div>
                  <button type="submit">Submit</button>
                </form>
          </div>
        );
    }
}
ReactDOM.render(React.createElement(UserForm), document.querySelector('#root'));