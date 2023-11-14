DROP TABLE IF EXISTS stock_data;
DROP TABLE IF EXISTS stock_share_prices;

CREATE TABLE stock_data(
  `stock_id` INT NOT NULL,
  `symbol` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `desc` TEXT(1000) NOT NULL,
  `CIK` VARCHAR(10) NOT NULL,
  `currency` VARCHAR(5) NOT NULL,
  `country` VARCHAR(5) NOT NULL,
  `sector` VARCHAR(20) NOT NULL,
  `industry` VARCHAR(45) NOT NULL,
  `address` VARCHAR(100) NOT NULL,
  `fiscal_year_end` VARCHAR(15) NOT NULL,
  `latest_qtr` DATE NOT NULL,
  `market_capitalization` VARCHAR(20) NOT NULL,
  `EBITDA` BIGINT(255) NOT NULL,
  `PERatio` VARCHAR(20) NOT NULL,
  `PEGRatio` VARCHAR(20) NOT NULL,
  `book_value` VARCHAR(20) NOT NULL,
  `div_per_share` VARCHAR(20) NOT NULL,
  `div_yield` VARCHAR(20) NOT NULL,
  `EPS` VARCHAR(20) NOT NULL,
  `rev_per_shareTTM` VARCHAR(20) NOT NULL,
  `profit_margin` VARCHAR(20) NOT NULL,
  `op_marginTTM` VARCHAR(20) NOT NULL,
  `return_on_assetsTTM` VARCHAR(20) NOT NULL,
  `return_on_equityTTM` VARCHAR(20) NOT NULL,
  `revenueTTM` VARCHAR(20) NOT NULL,
  `gross_profitTTM` VARCHAR(20) NOT NULL,
  `dilutedEPSTTM` VARCHAR(20) NOT NULL,
  `qtrly_earnings_growthYOY` VARCHAR(20) NOT NULL,
  `qtrly_revenue_growthYOY` VARCHAR(20) NOT NULL,
  `analyst_target_price` VARCHAR(20) NOT NULL,
  `trailingPE` VARCHAR(20) NOT NULL,
  `forwardPE` VARCHAR(20) NOT NULL,
  `price_to_sales_ratioTTM` VARCHAR(20) NOT NULL,
  `price_to_book_ratio` VARCHAR(20) NOT NULL,
  `EV_to_revenue` VARCHAR(20) NOT NULL,
  `EV_to_EBITDA` VARCHAR(20) NOT NULL,
  `beta` VARCHAR(20) NOT NULL,
  `week_high_52` VARCHAR(20) NOT NULL,
  `week_low_52` VARCHAR(20) NOT NULL,
  `day_moving_average_50` VARCHAR(20) NOT NULL,
  `day_moving_average_200` VARCHAR(20) NOT NULL,
  `shares_outstanding` VARCHAR(20) NOT NULL,
  `div_date` DATE NOT NULL,
  `ex_div_date` DATE NOT NULL,
  `last_updated` DATE NOT NULL,
  PRIMARY KEY (`stock_id`));
  
  CREATE TABLE stock_share_prices(
  `stock_id` INT NOT NULL,
  `time` DATE NOT NULL,
  `open` DOUBLE NOT NULL,
  `high` DOUBLE NOT NULL,
  `low` DOUBLE NOT NULL,
  `close` DOUBLE NOT NULL,
  `volume` DOUBLE NOT NULL,
  PRIMARY KEY (`stock_id`, `time`),
  CONSTRAINT `ssp_sd`
    FOREIGN KEY (`stock_id`)
    REFERENCES `stock_data` (`stock_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

    CREATE TABLE company_info(
    `stock_id` INT NOT NULL,
    'ceo' VARCHAR(50) NOT NULL,
    'website' VARCHAR(200) NOT NULL,
    'employees' VARCHAR(10) NOT NULL,
    'founded_year' VARCHAR(4) NOT NULL,
    'isin' VARCHAR(12) NOT NULL,
    PRIMARY KEY (`stock_id`),
    CONSTRAINT `ci_sd`
      FOREIGN KEY (`stock_id`)
      REFERENCES `stock_data` (`stock_id`)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION);
