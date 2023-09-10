import React from "react";
import { useNavigate } from "react-router-dom";

function Result () {
  var percent = 0
  const navigate = useNavigate();
  const Img = window.localStorage.getItem("Img")
  console.log("Image file : ", Img);

  const returnMain = () => {
    navigate('/')
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
          AI 판별 결과 당신의 충치 확률은 {percent}%입니다.
        </div>
        <div>
          해당 검사는 간단한 점검 및 관리 목적으로만 사용하시는 것을  추천드리며,
        </div>
        <div>
          보다 정밀한 진단 및 치료를 위해서는 치과 방문을 권장드립니다.
        </div>
        <div className="example">
          <img src={Img} alt="tooth"></img>
        </div>
        <button onClick={returnMain}>돌아 가기</button>
      </div>
    </React.Fragment>
  )

}

export default Result;