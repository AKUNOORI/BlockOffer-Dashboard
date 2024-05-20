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

// import React, { useState, useEffect } from 'react';
// import axios from 'axios';
// import Filters from './filter.jsx';
// import Chart from './Chart.jsx'

// function App() {
//     const [data, setData] = useState([]);
//     const [filters, setFilters] = useState({
//         year: '',
//         topic: '',
//         sector: '',
//         region: '',
//         pest: '',
//         source: '',
//         swot: '',
//         country: '',
//         city: ''
//     });

//     useEffect(() => {
//         fetchData();
//     }, [filters]);

//     const fetchData = async () => {
//         const params = new URLSearchParams(filters);
//         const response = await axios.get('http://localhost:8000/api/visualization/');
//         setData(response.data);
//     };

//     const updateFilters = (newFilters) => {
//         setFilters({ ...filters, ...newFilters });
//     };

//     return (
//         <div className="App">
//             <Filters filters={filters} updateFilters={updateFilters} />
//             <Chart data={data} />
//         </div>
//     );
// }

// export default App;
