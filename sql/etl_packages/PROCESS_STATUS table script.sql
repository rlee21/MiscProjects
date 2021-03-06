DROP TABLE EDW.PROCESS_STATUS CASCADE CONSTRAINTS;

CREATE TABLE EDW.PROCESS_STATUS
(
  BATCH_ID            NUMBER                    NOT NULL,
  SCHEMA_NAME         VARCHAR2(30 BYTE)         NOT NULL,
  PACKAGE_NAME        VARCHAR2(100 BYTE)        NOT NULL,
  PROGRAM_NAME        VARCHAR2(100 BYTE)        NOT NULL,
  PROGRAM_STATUS      VARCHAR2(1 BYTE)          NOT NULL,
  PROGRAM_START_DATE  DATE                      NOT NULL,
  PROGRAM_END_DATE    DATE,
  COMMENTS            VARCHAR2(2000 BYTE),
  ERROR_MESSAGE       VARCHAR2(500 BYTE),
  REC_INSERT_DATE     DATE                      DEFAULT sysdate
)
TABLESPACE EDW_DATA
RESULT_CACHE (MODE DEFAULT)
PCTUSED    0
PCTFREE    10
INITRANS   1
MAXTRANS   255
STORAGE    (
            INITIAL          64K
            NEXT             1M
            MINEXTENTS       1
            MAXEXTENTS       UNLIMITED
            PCTINCREASE      0
            BUFFER_POOL      DEFAULT
            FLASH_CACHE      DEFAULT
            CELL_FLASH_CACHE DEFAULT
           )
LOGGING 
NOCOMPRESS 
NOCACHE
NOPARALLEL
MONITORING;


--GRANT SELECT ON EDW.PROCESS_STATUS TO DM_INT_RO;
--
--GRANT DELETE, INSERT, SELECT, UPDATE ON EDW.PROCESS_STATUS TO DM_INT_RW;
