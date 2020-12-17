CREATE TABLE `Users` (
  `UserID` varchar(32) NOT NULL,
  `Email` varchar(80) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `DOB` date DEFAULT NULL,
  `FirstName` varchar(40) DEFAULT NULL,
  `LastName` varchar(40) DEFAULT NULL,
  `CreatedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `Username` (`Username`)
);
