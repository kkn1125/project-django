-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema scheduler
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema scheduler
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `scheduler` DEFAULT CHARACTER SET utf8 ;
USE `scheduler` ;

-- -----------------------------------------------------
-- Table `scheduler`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scheduler`.`user` (
  `num` INT NOT NULL AUTO_INCREMENT,
  `profile` VARCHAR(150) NULL DEFAULT '',
  `nickname` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `regdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updates` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`num`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `scheduler`.`room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scheduler`.`room` (
  `num` INT NOT NULL AUTO_INCREMENT,
  `master` INT NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `regdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updates` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`num`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `scheduler`.`user_in_room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scheduler`.`user_in_room` (
  `num` INT NOT NULL AUTO_INCREMENT,
  `room_num` INT NOT NULL,
  `user_num` INT NOT NULL,
  PRIMARY KEY (`num`),
  INDEX `fk_user_in_room_room_idx` (`room_num` ASC) VISIBLE,
  INDEX `fk_user_in_room_user1_idx` (`user_num` ASC) VISIBLE,
  CONSTRAINT `fk_user_in_room_room`
    FOREIGN KEY (`room_num`)
    REFERENCES `scheduler`.`room` (`num`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_in_room_user1`
    FOREIGN KEY (`user_num`)
    REFERENCES `scheduler`.`user` (`num`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `scheduler`.`calendar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `scheduler`.`calendar` (
  `num` INT NOT NULL AUTO_INCREMENT,
  `room_num` INT NOT NULL,
  `user_num` INT NOT NULL,
  `category` VARCHAR(45) NOT NULL,
  `title` VARCHAR(50) NOT NULL,
  `schedule` TEXT NOT NULL,
  `coworker` VARCHAR(200) NULL DEFAULT '',
  `start_date` TIMESTAMP NOT NULL,
  `end_date` TIMESTAMP NOT NULL,
  `regdate` TIMESTAMP NOT NULL,
  `updates` TIMESTAMP NOT NULL,
  PRIMARY KEY (`num`),
  INDEX `fk_calendar_room1_idx` (`room_num` ASC) VISIBLE,
  INDEX `fk_calendar_user1_idx` (`user_num` ASC) VISIBLE,
  CONSTRAINT `fk_calendar_room1`
    FOREIGN KEY (`room_num`)
    REFERENCES `scheduler`.`room` (`num`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_calendar_user1`
    FOREIGN KEY (`user_num`)
    REFERENCES `scheduler`.`user` (`num`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

use scheduler;
show tables;