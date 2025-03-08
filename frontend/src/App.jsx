import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './components/auth/LoginForm';
import Register from './components/auth/RegisterForm';
import Profile from './components/Profile';
import StudioList from './components/studio/StudioList';
import Booking from './pages/studio/Booking';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route
                    path="/profile"
                    element={
                            <Profile />
                    }
                />
                <Route path="/studios" element={<StudioList />} />
                <Route path="/booking/:id" element={<Booking />} />
            </Routes>
        </Router>
    );
};

export default App;