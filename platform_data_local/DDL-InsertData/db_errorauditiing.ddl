DROP TABLE IF EXISTS MAIN.ERROR_AUDITING;
create table main.ERROR_AUDITING
(
    AUDIT_ID          INTEGER primary key autoincrement,
    AUDIT_TYPE        VARCHAR(15),
    AUDIT_DATE        VARCHAR(19),
    AUDIT_TIME        VARCHAR(19),
    AUDIT_COMPONENT   VARCHAR(99),
    TRANSACTION_COUNT INT,
    AUDIT_DETAILS     VARCHAR(75),
    ERROR_ID          VARCHAR(99),
    ERROR_DESC        VARCHAR(99),
    PROCESSED_OBJECT  VARCHAR(149),
    AUDIT_DATETIME    VARCHAR(40),
    START_DATETIME    varchar(30),
    END_DATETIME      varchar(30),
    AUDIT_OPERATION   varchar(99)
);
