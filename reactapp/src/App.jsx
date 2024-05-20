
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PostData from './postData.jsx'

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<PostData />} />
            </Routes>
        </Router>
    );
};

export default App;

