CREATE TABLE PASSWORD_RESET(
   RESET_CODE  TEXT      NOT NULL,
   USER_ID     TEXT      NOT NULL,
   USER_NAME   TEXT      NOT NULL,
   EMAIL       TEXT      NOT NULL,
   CREATE_TIMESTAMP TIMESTAMP      NOT NULL, 
   EXPIRY_TIMESTAMP TIMESTAMP      NOT NULL
   
);

