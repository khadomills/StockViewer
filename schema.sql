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
  `market_capitalization` BIGINT(255) NOT NULL,
  `EBITDA` BIGINT(255) NOT NULL,
  `PERatio` DOUBLE NOT NULL,
  `PEGRatio` DOUBLE NOT NULL,
  `book_value` DOUBLE NOT NULL,
  `div_per_share` DOUBLE NOT NULL,
  `div_yield` DOUBLE NOT NULL,
  `EPS` DOUBLE NOT NULL,
  `rev_per_shareTTM` DOUBLE NOT NULL,
  `profit_margin` DOUBLE NOT NULL,
  `op_marginTTM` DOUBLE NOT NULL,
  `return_on_assetsTTM` DOUBLE NOT NULL,
  `return_on_equityTTM` DOUBLE NOT NULL,
  `revenueTTM` BIGINT(255) NOT NULL,
  `gross_profitTTM` BIGINT(255) NOT NULL,
  `dilutedEPSTTM` DOUBLE NOT NULL,
  `qtrly_earnings_growthYOY` DOUBLE NOT NULL,
  `qtrly_revenue_growthYOY` DOUBLE NOT NULL,
  `analyst_target_price` DOUBLE NOT NULL,
  `trailingPE` DOUBLE NOT NULL,
  `forwardPE` DOUBLE NOT NULL,
  `price_to_sales_ratioTTM` DOUBLE NOT NULL,
  `price_to_book_ratio` DOUBLE NOT NULL,
  `EV_to_revenue` DOUBLE NOT NULL,
  `EV_to_EBITDA` DOUBLE NOT NULL,
  `beta` DOUBLE NOT NULL,
  `week_high_52` DOUBLE NOT NULL,
  `week_low_52` DOUBLE NOT NULL,
  `day_moving_average_50` DOUBLE NOT NULL,
  `day_moving_average_200` DOUBLE NOT NULL,
  `shares_outstanding` BIGINT(255) NOT NULL,
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