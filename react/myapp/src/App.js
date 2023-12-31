
import './App.css';
import Header from 'C:/Users/chara/OneDrive/Desktop/GLOBAL COURSE/react/myapp/src/components/Header.js';
import Content from 'C:/Users/chara/OneDrive/Desktop/GLOBAL COURSE/react/myapp/src/components/Content.js';
import Footer from 'C:/Users/chara/OneDrive/Desktop/GLOBAL COURSE/react/myapp/src/components/Footer.js';
import Customer from 'C:/Users/chara/OneDrive/Desktop/GLOBAL COURSE/react/myapp/src/components/Customer.js';
import Calculate1 from './components/Calculate1';
import UseEffectDemo from './components/UseEffectDemo';
import PostAPI from './components/PostAPI';
import EmployeeMaster from './components/EmployeeMaster';
import Productmaster from './components/productmaster';
function App() {
  return (
    <div className="App">
      <Header/> 
      <Content/>
      <Footer/>
      <Customer/>
      <Calculate1/>
      <UseEffectDemo/>
      <PostAPI/>
      <EmployeeMaster/>
      <Productmaster/>
    </div>
  );
}

export default App;
