import React, { Component } from 'react';
//import logo from './logo.svg';
//import './App.css';

class App extends Component {
    state = {
        todos: []
    };
    
    async componentDidMount(){
        try{
            const data = await fetch('http://127.0.0.1:8000/api/');
            const todos = await data.json();
            this.setState({todos});
        }catch (err){
            console.log(err);
        }
    }
    
    render(){
        return (
            <div className="App">
                {this.state.todos.map(field => (
                    <div key={field.id}>
                        <h1> {field.title} </h1>
                        <p> {field.description} </p>
                    </div>
                ))}
            </div>
        );
    }
}

export default App;
