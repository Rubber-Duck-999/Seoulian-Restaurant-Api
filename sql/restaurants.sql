CREATE TABLE `Restaurants` (
  `RestaurantID` varchar(32) NOT NULL,
  `RestaurantName` varchar(32) DEFAULT NULL,
  `Cuisine` varchar(20) DEFAULT NULL,
  `Postcode` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`RestaurantID`)
);
