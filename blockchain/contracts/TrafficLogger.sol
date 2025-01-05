// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TrafficLogger {
    struct TrafficData {
        string userID;
        string role;
        string filePath;
        uint256 behaviorProbability; // Store as a scaled integer (e.g., 15 for 0.15)
        bool accessGranted;
    }

    TrafficData[] public trafficLogs;

    // Log traffic data
    function logTrafficData(
        string memory _userID,
        string memory _role,
        string memory _filePath,
        uint256 _behaviorProbability, // Pass as an integer scaled by 100 (e.g., 15 for 0.15)
        bool _accessGranted
    ) public {
        TrafficData memory newLog = TrafficData({
            userID: _userID,
            role: _role,
            filePath: _filePath,
            behaviorProbability: _behaviorProbability,
            accessGranted: _accessGranted
        });
        trafficLogs.push(newLog);
    }

    // Retrieve a specific traffic log
    function getTrafficData(uint256 index)
        public
        view
        returns (
            string memory,
            string memory,
            string memory,
            uint256,
            bool
        )
    {
        require(index < trafficLogs.length, "Index out of bounds");
        TrafficData memory log = trafficLogs[index];
        return (
            log.userID,
            log.role,
            log.filePath,
            log.behaviorProbability,
            log.accessGranted
        );
    }

    // Get the total number of logs
    function trafficLogsLength() public view returns (uint256) {
        return trafficLogs.length;
    }
}

