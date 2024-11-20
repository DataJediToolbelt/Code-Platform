drop table if exists main.configuration_datasources;
create table main.configuration_datasources
(
    datasources_id integer
        primary key autoincrement,
    datasource_name         TEXT,
    datasource_type         TEXT,
    created_date            TEXT    default (datetime('now', 'localtime')),
    status_id               integer default 1,
    host TEXT,
    port INT,
    additional_details TEXT,
    custom_url TEXT,
    app_token TEXT,
    custom_token TEXT,
    bearer_token TEXT,
    uid            TEXT,
    pwd TEXT,
    organization_guid       TEXT,
    registeredapp_guid      TEXT
);

drop table if exists configuration_settings;
create table configuration_settings
(
    config_param_name TEXT,
    config_param_type TEXT,
    config_detail     TEXT
);
