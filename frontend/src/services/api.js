// services/api.js

// Аутентификация
export const login = async (username, password) => {
  return new Promise(resolve => {
    setTimeout(() => resolve({
      access_token: 'fake_token',
      refresh_token: 'fake_refresh',
      user: {
        id: 1,
        username: username,
        is_musician: true,
        is_studio_owner: false
      }
    }), 1000);
  });
};

export const register = async (userData) => {
  return new Promise(resolve => {
    setTimeout(() => resolve({ success: true }), 1000);
  });
};

// Профиль
export const getProfile = async () => {
  return new Promise(resolve => {
    setTimeout(() => resolve({
      id: 1,
      user: {
        id: 1,
        username: 'john_doe',
        email: 'john@example.com'
      },
      bio: 'Music producer and sound engineer',
      avatar: '/avatar1.jpg',
      social_links: ['https://soundcloud.com/johndoe']
    }), 1000);
  });
};

// Студии
export const getStudios = async () => {
  return new Promise(resolve => {
    setTimeout(() => resolve([
      {
        id: 1,
        name: 'Studio A',
        address: '123 Music St',
        price_per_hour: 50,
        image: '/studio1.jpg',
        equipment: ['Microphone', 'Mixer', 'DAW']
      },
      {
        id: 2,
        name: 'Studio B',
        address: '456 Beat Ave',
        price_per_hour: 75,
        image: '/studio2.jpg',
        equipment: ['Synthesizer', 'Drum Kit']
      }
    ]), 1000);
  });
};

// Бронирование
export const bookStudio = async (studioId, dateTime) => {
  return new Promise(resolve => {
    setTimeout(() => resolve({
      id: Date.now(),
      studio: { id: studioId },
      user: { id: 1 },
      time: dateTime,
      status: 'confirmed'
    }), 1000);
  });
};

// Коллаборации
export const getCollaborations = async () => {
  return new Promise(resolve => {
    setTimeout(() => resolve([
      {
        id: 101,
        project_name: 'Summer Hit',
        participants: ['john_doe', 'jane_doe'],
        status: 'active',
        created_at: '2024-03-01T10:00:00Z'
      },
      {
        id: 102,
        project_name: 'Jazz Album',
        participants: ['john_doe', 'musician22'],
        status: 'pending',
        created_at: '2024-03-02T15:30:00Z'
      }
    ]), 1000);
  });
};

// История бронирований
export const getBookings = async () => {
  return new Promise(resolve => {
    setTimeout(() => resolve([
      {
        id: 201,
        studio: { name: 'Studio A' },
        time: '2024-03-05T14:00:00Z',
        status: 'completed'
      },
      {
        id: 202,
        studio: { name: 'Studio B' },
        time: '2024-03-06T10:00:00Z',
        status: 'upcoming'
      }
    ]), 1000);
  });
};