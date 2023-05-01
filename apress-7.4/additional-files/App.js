import React from 'react';
import Button from '@material-ui/core/Button'; // Material-UI, the world's most popular React UI framework

import logo from './logo.svg';
import './App.css';
import './Dnd.css';

import $ from 'jquery';




class App extends React.Component {
 
  constructor(props) {
    super(props);
    this.state = {
      file: '',
      files: [],
      imagePreviewUrl: ''
    };
    this._handleImageChange = this._handleImageChange.bind(this);
    this._handleSubmit = this._handleSubmit.bind(this);
  }

  _handleSubmit(e) {
    e.preventDefault();
    // TODO: do something with -> this.state.file
  }

  _handleImageChange(e) {
    e.preventDefault();

    let reader = new FileReader();
    let file = e.target.files[0];

    reader.onloadend = () => {
      this.setState({
        file: file,
        imagePreviewUrl: reader.result
      });
    }

    reader.readAsDataURL(file)
  }

  onPreviewDrop = (files) => {
    this.setState({
      files: this.state.files.concat(files),
     });
     alert("Great Shot!")
  }


  render() {

    let {imagePreviewUrl} = this.state;
    let $imagePreview = null;
    if (imagePreviewUrl) {
      $imagePreview = (<img id='uploadedImage' name='formUpload' src={imagePreviewUrl} thumbnail />);
    } else {
      // $imagePreview = (<div className="previewText">Please select an Image for Preview</div>);
    }


      return (
        
        <div className="App">
      
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Traffic Sign Classification</h2>
        </header>
        
        <form method="POST" action="" enctype="multipart/form-data" id='mainForm'>
            <p style={{color: imagePreviewUrl ? 'transparent' : '#ffffff'}} >Drag your files here or click in this area.</p>
            <input type="file" name="file" multiple onChange={this._handleImageChange} ></input>
            <button onClick={this._handleSubmit}>UPLOAD IMAGE</button>
            <input type="submit" value="Submit" ></input>
            <Button className='submitBtns' style={{backgroundColor: "#90caf9"}} variant="contained" type="submit" value="Submit" onDrop={this._onPreviewDrop}>Run Script</Button>
            <Button className='submitBtns' style={{backgroundColor: "#f48fb1"}} variant="contained"
            href="https://mybinder.org/v2/gh/ChangingEnergy/DL_MalariaClassification_TrainingOnly/master?filepath=DeepLearning_trainingOnly.ipynb"            target="_blank" >
              Train Model
            </Button> 

            {$imagePreview}
            <div> </div>
            <div id='inferMsg' style={{color: imagePreviewUrl ? 'transparent': '#ffffff' }}> {window.token}</div>
        </form>


        
  
  
  
  
      </div>

      );
  }
}

export default App;