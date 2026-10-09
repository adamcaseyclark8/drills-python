r"""TODO: port to Python.

Original JavaScript (code/misc/claude-jest-example.js):

class ApiClient {
    async fetchUser(userId) {
        // Simulates API call
        const response = await fetch(`https://api.example.com/users/${userId}`);
        return response.json();
    }

    async saveUser(userData) {
        // Simulates saving to API
        const response = await fetch('https://api.example.com/users', {
            method: 'POST',
            body: JSON.stringify(userData)
        });
        return response.json();
    }
}

class UserService {
    constructor(apiClient) {
        this.apiClient = apiClient;
        this.cache = new Map();
    }

    async getUserWithCache(userId) {
        // Check cache first
        if (this.cache.has(userId)) {
            return this.cache.get(userId);
        }

        // Fetch from API if not cached
        const user = await this.apiClient.fetchUser(userId);
        this.cache.set(userId, user);
        return user;
    }

    async updateUserAge(userId, newAge) {
        const user = await this.getUserWithCache(userId);

        if (newAge < 0 || newAge > 150) {
            throw new Error('Invalid age');
        }

        const updatedUser = { ...user, age: newAge };
        await this.apiClient.saveUser(updatedUser);

        // Update cache
        this.cache.set(userId, updatedUser);
        return updatedUser;
    }

    clearCache() {
        this.cache.clear();
    }
}

module.exports = { ApiClient, UserService };

"""
