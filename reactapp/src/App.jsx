// import React from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import VisualizationComponent from './VisualizationComponent.jsx'
// import PostData from './postData.jsx'


// function App() {

//   return (
//     <>
//     <PostData/>
//     <VisualizationComponent/>
//     </>
//   )
// }

// export default App


import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PostData from './postData.jsx'

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<PostData />} />
                {/* <Route path="/VisualizationComponent" element={<VisualizationComponent />} /> */}
            </Routes>
        </Router>
    );
};

export default App;

