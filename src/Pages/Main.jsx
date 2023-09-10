import React, { useRef, useState } from "react";
import axios from 'axios';
import Preview from '../Images/preview.png'
import '../css/Main.scss'
import ex1 from '../Images/ex1.jpg'
import ex2 from '../Images/ex2.jpg'
import ex3 from '../Images/ex3.jpg'
import { useNavigate } from "react-router-dom";

function Main () {
  const navigate = useNavigate();
  const imgRef = useRef();
  const [imgFile, setImgFile] = useState(null);
  const [previewImg, setPreviewImg] = useState(null);

  const fileUpload = (e) => {
    const file = e.target.files;
    const previewFile = imgRef.current.files[0];
    if(previewFile)
    {
      const render = new FileReader();
      render.readAsDataURL(previewFile)
  
      render.onloadend = () => {
        setPreviewImg(render.result)
      }
  
      for(var i = 0; i < (file).length; i++) {
        console.log("test:", file[i]);
      }
  
      setImgFile(file)
      window.localStorage.setItem("Img", file[0])
      const temp = window.localStorage.getItem("Img")
      console.log(temp);
    }
    else {
      setPreviewImg(Preview)
    }

  }

  const sendFile = async() => {
    const formdata = new FormData();

    if(imgFile) {
      Object.values(imgFile).forEach((imgFile) => formdata.append("file", imgFile))
    }
    else {
      console.log("No File");
      navigate('/result')
      return 0;
    }

    try {
      const res = await axios
      .post(
        "http://localhost:8080/file",
        formdata
      )
      .then((response) => {
        console.log("Send Complete!");
        console.log("File Response: ", response)
        navigate('/result')
      })
    }
    catch(e) {
      console.log("File send ERROR", e);
    }
  }


  return (
    <React.Fragment>
      <div className="container">
        <header>
          <h1>
            HOME DENTAL SERVICE
          </h1>
          <h2>
            집에서 간편하게 하는 치아관리
          </h2>
        </header>
        <div>
          예시 사진을 참고하여 치아 사진을 찍고 업로드하면
          AI가 충치 여부를 판별해 줍니다.
        </div>
        <div className="example">
          <img src={ex1}></img>
          <img src={ex2}></img>
          <img src={ex3}></img>
        </div>
        <div className="preview">
          <img className="previewImg"  src={previewImg ? previewImg : Preview}></img>
          <input type="file" name='file' ref={imgRef} id="FileUpload" accept="image/png, image/jpeg, image/jpg" onChange={fileUpload}></input>
        </div>
        <button onClick={sendFile}>결과 보기</button>
      </div>
    </React.Fragment>
  )
}

export default Main;