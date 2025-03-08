// pages/Profile.jsx
import { useEffect, useState } from 'react';
import { getProfile } from '../services/api';

const Profile = () => {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      const data = await getProfile();
      setProfile(data);
    };
    fetchProfile();
  }, []);

  if (!profile) return <div>Loading...</div>;

  return (
    <div>
      <img src={profile.avatar} alt="Avatar" />
      <h2>{profile.user.username}</h2>
      <p>{profile.bio}</p>
      <div>Social: {profile.social_links.join(', ')}</div>
    </div>
  );
};