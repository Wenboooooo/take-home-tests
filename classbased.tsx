import React, { useState, useEffect } from 'react';

type User = {
    name: string;
    email: string;
};

type UserDataProps = {
    userId: string;
};

const UserData: React.FC<UserDataProps> = ({ userId }) => {
    const [user, setUser] = useState<User | null>(null);
    const [seconds, setSeconds] = useState(0);

    useEffect(() => {
        // Function to fetch user data
        const fetchUserData = () => {
            fetch(`https://secret.url/user/${userId}`)
                .then((response) => response.json())
                .then((data) => setUser(data))
                .catch((error) => console.error('Error fetching user data:', error));
        };

        // Fetch user data initially
        fetchUserData();

        // Start the timer
        const intervalId = setInterval(() => {
            setSeconds((prevSeconds) => prevSeconds + 1);
        }, 1000);

        // Cleanup function to clear interval when component unmounts
        return () => {
            clearInterval(intervalId);
        };
    }, [userId]); // Effect will run whenever userId changes

    return (
        <div>
            <h1>User Data Component</h1>
    {user ? (
        <div>
            <p>Name: {user.name}</p>
        <p>Email: {user.email}</p>
    </div>
    ) : (
        <p>Loading user data...</p>
    )}
    <p>Timer: {seconds} seconds</p>
    </div>
);
};

export default UserData;



// Key changes:
// State management: Replaced the state with useState hooks for user and seconds.
// Lifecycle methods: Replaced componentDidMount and componentDidUpdate with useEffect and the clearInterval function replaces componentWillUnmount.
// Fetching data: Moved the fetchUserData function inside the useEffect hook, and it triggers whenever userId changes, mimicking the behavior of componentDidUpdate.
