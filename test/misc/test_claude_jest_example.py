r"""TODO: port to Python.

Original JavaScript (test/misc/claude-jest-example.test.js):

const { ApiClient, UserService } = require('../../code/misc/claude-jest-example.js');

describe('UserService', () => {
    let apiClient;
    let userService;
    let fetchUserSpy;
    let saveUserSpy;

    beforeEach(() => {
        apiClient = new ApiClient();
        userService = new UserService(apiClient);

        // Spy on API methods and mock their implementations
        fetchUserSpy = jest.spyOn(apiClient, 'fetchUser').mockImplementation(userId => {
            return Promise.resolve({
                id: userId,
                name: 'John Doe',
                age: 30,
                email: 'john@example.com'
            });
        });

        saveUserSpy = jest.spyOn(apiClient, 'saveUser').mockImplementation(userData => {
            return Promise.resolve({ ...userData, saved: true });
        });
    });

    afterEach(() => {
        fetchUserSpy.mockRestore();
        saveUserSpy.mockRestore();
    });

    describe('getUserWithCache', () => {
        test('fetches user from API on first call', async () => {
            const user = await userService.getUserWithCache(1);

            expect(fetchUserSpy).toHaveBeenCalledTimes(1);
            expect(fetchUserSpy).toHaveBeenCalledWith(1);
            expect(user).toEqual({
                id: 1,
                name: 'John Doe',
                age: 30,
                email: 'john@example.com'
            });
        });

        test('returns cached user on second call without fetching', async () => {
            // First call
            await userService.getUserWithCache(1);

            // Second call
            const user = await userService.getUserWithCache(1);

            // API should only be called once
            expect(fetchUserSpy).toHaveBeenCalledTimes(1);
            expect(user.name).toBe('John Doe');
        });

        test('fetches different users separately', async () => {
            await userService.getUserWithCache(1);
            await userService.getUserWithCache(2);

            expect(fetchUserSpy).toHaveBeenCalledTimes(2);
            expect(fetchUserSpy).toHaveBeenNthCalledWith(1, 1);
            expect(fetchUserSpy).toHaveBeenNthCalledWith(2, 2);
        });

        test('clears cache properly', async () => {
            await userService.getUserWithCache(1);
            userService.clearCache();
            await userService.getUserWithCache(1);

            // Should fetch twice since cache was cleared
            expect(fetchUserSpy).toHaveBeenCalledTimes(2);
        });
    });

    describe('updateUserAge', () => {
        test('fetches user, updates age, and saves', async () => {
            const updatedUser = await userService.updateUserAge(1, 35);

            expect(fetchUserSpy).toHaveBeenCalledWith(1);
            expect(saveUserSpy).toHaveBeenCalledWith({
                id: 1,
                name: 'John Doe',
                age: 35,
                email: 'john@example.com'
            });
            expect(updatedUser.age).toBe(35);
        });

        test('throws error for negative age', async () => {
            await expect(userService.updateUserAge(1, -5)).rejects.toThrow('Invalid age');

            expect(saveUserSpy).not.toHaveBeenCalled();
        });

        test('throws error for age over 150', async () => {
            await expect(userService.updateUserAge(1, 200)).rejects.toThrow('Invalid age');

            expect(saveUserSpy).not.toHaveBeenCalled();
        });

        test('updates cache after saving', async () => {
            await userService.updateUserAge(1, 40);

            // Get user again - should use cached updated value
            const user = await userService.getUserWithCache(1);

            // fetchUser should only be called once (during update)
            expect(fetchUserSpy).toHaveBeenCalledTimes(1);
            expect(user.age).toBe(40);
        });

        test('uses cached user if available', async () => {
            // Pre-populate cache
            await userService.getUserWithCache(1);

            // Update age
            await userService.updateUserAge(1, 45);

            // Should still only fetch once (from first call)
            expect(fetchUserSpy).toHaveBeenCalledTimes(1);
            expect(saveUserSpy).toHaveBeenCalledTimes(1);
        });
    });

    describe('spy with different mock return values', () => {
        test('handles API errors gracefully', async () => {
            fetchUserSpy.mockRejectedValueOnce(new Error('Network error'));

            await expect(userService.getUserWithCache(1)).rejects.toThrow('Network error');
        });

        test('can mock different users for different IDs', async () => {
            fetchUserSpy
                .mockResolvedValueOnce({ id: 1, name: 'Alice', age: 25 })
                .mockResolvedValueOnce({ id: 2, name: 'Bob', age: 30 });

            const user1 = await userService.getUserWithCache(1);
            const user2 = await userService.getUserWithCache(2);

            expect(user1.name).toBe('Alice');
            expect(user2.name).toBe('Bob');
        });
    });

    // EXAMPLE EXPLAINING SPIES AND MOCKS AND SPIES + MOCKS
    //
    // describe('UserService - Using Mocked Spies', () => {
    //     // Setup: Create spies and add mock implementations
    //     fetchUserSpy = jest
    //         .spyOn(apiClient, 'fetchUser')           // SPY: Watch the method
    //         .mockImplementation((userId) => {        // MOCK: Fake the behavior
    //             return Promise.resolve({ id: userId });
    //         });
    //
    //     // Use SPY capabilities to verify behavior
    //     test('verifies API call count', async () => {
    //         await userService.getUserWithCache(1);
    //         expect(fetchUserSpy).toHaveBeenCalledTimes(1);  // Using spy tracking
    //     });
    //
    //     // Use MOCK capabilities to control output
    //     test('returns controlled fake data', async () => {
    //         const user = await userService.getUserWithCache(1);
    //         expect(user.id).toBe(1);  // Got our mocked data, not real API
    //     });
    // });
});

"""
