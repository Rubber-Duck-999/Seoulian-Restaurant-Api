CREATE TABLE `Posts` (  
    `PostID` varchar(32) NOT NULL,
    `UserID` varchar(32) DEFAULT NULL,
    `CreatedDate` datetime DEFAULT NULL,
    `Validated` tinyint(1) DEFAULT,
    `SQLKey` varchar(32) NOT NULL,
    `RestaurantID` varchar(32) DEFAULT NULL,
    PRIMARY KEY (`PostID`),
    UNIQUE KEY `SQLKey` (`SQLKey`),
    KEY `UserID` (`UserID`),
    KEY `RestaurantID` (`RestaurantID`),
    CONSTRAINT `Posts_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`),
    CONSTRAINT `Posts_ibfk_2` FOREIGN KEY (`RestaurantID`) REFERENCES `Restaurants` (`RestaurantID`)
);
