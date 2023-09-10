import { BrowserRouter, Route, Link, Routes} from 'react-router-dom'
import './App.css';
import Main from './Pages/Main'
import Result from './Pages/Resule'

function App() {
  return (
    <BrowserRouter basename='/'>
      <Routes>
        <Route path='/' exact element={<Main />}></Route>
        <Route path='/result' exact element={<Result />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
