drop table if exists main.configuration_details;
create table main.configuration_details
(
    config_param_name varchar(49) primary key,
    config_param_type varchar(19),
    config_detail     varchar(129)
);

drop table if exists main.platform_datasources;
create table main.platform_datasources
(
    datasources_id     integer primary key autoincrement,
    datasource_name    varchar(49),
    datasource_type    varchar(79),
    created_date      varchar(20)    default (datetime('now', 'localtime')),
    status_id          varchar(10) DEFAULT 'Active"',
    host               varchar(99),
    port               INT,
    additional_details varchar(129),
    custom_url         varchar(129),
    app_token          varchar(256),
    custom_token       varchar(256),
    bearer_token       varchar(256),
    uid                varchar(99),
    pwd                varchar(79),
    organization_guid  varchar(38),
    registeredapp_guid varchar(38)
);

drop table if exists main.platform_operations;
create table main.platform_operations
(
    operation_name varchar(39) primary key,
    operation_desc varchar(99),
    status_id      varchar(10)
);

