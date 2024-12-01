DROP TABLE IF EXISTS MAIN.ERROR_AUDITING;
CREATE TABLE MAIN.ERROR_AUDITING
(
    AUDIT_ID                INTEGER PRIMARY KEY AUTOINCREMENT,
    AUDIT_TYPE              VARCHAR(15)  NULL,
    AUDIT_DATETIME       VARCHAR(20) NULL,
    AUDIT_DATE              VARCHAR(19)  NULL,
    AUDIT_TIME              VARCHAR(19)  NULL,
    COMPONENT_NAME         VARCHAR(99)  NULL,
    OPERATION_NAME      VARCHAR(99) NULL,
    TRANSACTION_COUNT SMALLINT     NULL,
    AUDIT_DETAILS           VARCHAR(75)  NULL,
    ERROR_ID                VARCHAR(99)  NULL,
    ERROR_DESC              VARCHAR(99)  NULL,
    PROCESSED_OBJECT        VARCHAR(149) NULL
);