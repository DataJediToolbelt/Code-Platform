-- Create Tables
drop table if exists datatier_crawler;
CREATE TABLE datatier_crawler
(
    datacrawler_id      integer primary key autoincrement,
    token               TEXT,
    crawledtext_details text,
    created_date        TEXT    default (datetime('now', 'localtime')),
    status_id           integer DEFAULT 1,
    registeredapp_guid  TEXT,
    organization_guid   TEXT
);

DROP TABLE if exists datatier_sdp_datastructures;
CREATE TABLE datatier_sdp_datastructures
(
    datastructure_core_id integer primary key autoincrement,
    datastructure_name    TEXT,
    datastructure_details text,
    created_date          TEXT default (datetime('now', 'localtime')),
    status_id             integer   DEFAULT 1,
    registeredapp_guid    TEXT
);

drop table if exists datatier_sdp_dataattributes;
create table datatier_sdp_dataattributes
(
    datatier_id        integer primary key autoincrement,
    basevalue          TEXT,
    supportingvalue1   TEXT,
    supportingvalue2   TEXT,
    supportingvalue3   TEXT,
    supportingvalue4   TEXT,
    supportingvalue5   TEXT,
    supportingvalue6   TEXT,
    supportingvalue7   TEXT,
    created_date       TEXT,
    status_id          integer,
    dataattribute_id   integer,
    created_user       TEXT,
    registeredapp_guid TEXT,
    datagentype_id     integer
);

drop table if exists datatier_tokens;
CREATE TABLE datatier_tokens
(
    datatoken_id       integer primary key autoincrement,
    token              char(128),
    created_date       TEXT default (datetime('now', 'localtime')),
    status_id          integer   DEFAULT 1,
    registeredapp_guid TEXT,
    organization_guid  TEXT,
    intfc_type         TEXT      DEFAULT 'API',
    datasource_id      integer
);

DROP TABLE if exists datamodel_apis;
CREATE TABLE datamodel_apis
(
    api_id             integer primary key autoincrement,
    technology         TEXT,
    dataattributes_id  integer,
    baseurllocation    TEXT,
    apiname            TEXT,
    created_date       TEXT default (datetime('now', 'localtime')),
    status_id          integer   DEFAULT 1,
    purpose            TEXT,
    datmodel_tablename TEXT,
    apiparams          TEXT,
    apiexample         TEXT
);

DROP TABLE if exists datamodel_datatables;
CREATE TABLE datamodel_datatables
(
    tablename        TEXT NOT NULL,
    tableinformation TEXT,
    status_id        integer   DEFAULT 1,
    created_date     TEXT default (datetime('now', 'localtime')),
    datadomain       TEXT
);

DROP TABLE if exists datamodel_domain;
CREATE TABLE datamodel_domain
(
    domainname        TEXT NOT NULL,
    domaininformation TEXT,
    status_id         integer   DEFAULT 1,
    created_date      TEXT default (datetime('now', 'localtime'))
);

DROP TABLE if exists platform_codesets_crossmaps;
CREATE TABLE platform_codesets_crossmaps
(
    codesetcrossmap_id  integer primary key autoincrement,
    implcodesets_id     integer NOT NULL,
    application_guid    TEXT,
    organization_guid   TEXT,
    terminologystd_to   integer,
    created_date        TEXT default (datetime('now', 'localtime')),
    status_id           integer   DEFAULT 1,
    created_user        TEXT,
    transformcode_value TEXT,
    transformcode_desc  TEXT,
    originalcode_value  TEXT,
    originalcode_desc   TEXT
);

DROP TABLE if exists platform_dataattributes;
CREATE TABLE platform_dataattributes
(
    platform_dataattributes_id  integer primary key autoincrement,
    dataattribute_name          TEXT,
    sensitivityflag_id          integer,
    created_date                TEXT default (datetime('now', 'localtime')),
    status_id                   integer   DEFAULT 1,
    created_user                TEXT,
    platform_dataattribute_guid TEXT,
    registeredapp_guid          TEXT,
    attribute_type              TEXT
);

DROP TABLE if exists platform_datageneration;
CREATE TABLE platform_datageneration
(
    datagentype_id          integer primary key autoincrement,
    datagentype_description TEXT,
    definition              TEXT,
    dataattribute_id        integer,
    created_date            TEXT default (datetime('now', 'localtime')),
    status_id               integer   DEFAULT 1,
    created_user            TEXT,
    quantity                integer,
    maxrecordsinsource      integer,
    registeredapp_guid      TEXT,
    organization_guid       TEXT
);

drop table if exists platform_datasources;
create table platform_datasources
(
    platform_datasources_id integer primary key autoincrement,
    datasource_name         TEXT,
    datasource_type         TEXT,
    created_date            TEXT default (datetime('now', 'localtime')),
    status_id               integer   default 1,
    created_user            TEXT,
    organization_guid       TEXT,
    registeredapp_guid      TEXT
);

drop table if exists platform_datastructures;
create table platform_datastructures
(
    platform_datastructures_id   integer primary key autoincrement,
    datastructure_name           TEXT,
    sensitivityflag_id           integer,
    created_date                 TEXT default (datetime('now', 'localtime')),
    status_id                    integer   default 1,
    created_user                 TEXT,
    platform_datastructures_guid TEXT,
    registeredapp_guid           TEXT
);

drop table if exists platform_datastructures_dtl;
CREATE TABLE platform_datastructures_dtl
(
    platform_datastructuresdtl_id                  integer primary key autoincrement,
    platform_datastructures_id                     integer,
    composite_datastructure_name                   TEXT,
    sensitivityflag_id                             integer   DEFAULT 1,
    created_date                                   TEXT default (datetime('now', 'localtime')),
    status_id                                      integer   DEFAULT 1,
    created_user                                   TEXT,
    platform_datastructures_to_dataattributes_guid TEXT,
    registeredapp_guid                             TEXT,
    platform_dataattributes_id                     integer
);

drop table if exists platform_xmap_tokens_attributes_dtl;
CREATE TABLE platform_xmap_tokens_attributes_dtl
(
    platform_xmap_tokens_attributesdtl_id integer primary key autoincrement,
    platform_datastructures_id            integer,
    xmap_details                          TEXT,
    dataattribute_id                      integer   DEFAULT 1,
    fieldorder_id                         integer   DEFAULT 1,
    created_date                          TEXT default (datetime('now', 'localtime')),
    status_id                             integer   DEFAULT 1,
    created_user                          TEXT,
    registeredapp_guid                    TEXT,
    organization_guid                     TEXT
);

drop table if exists refdata_application;
CREATE TABLE refdata_application
(
    app_guid               TEXT primary key,
    application_customcode TEXT,
    application_desc       TEXT,
    created_user           TEXT,
    created_date           TEXT default (datetime('now', 'localtime')),
    status_id              integer   DEFAULT 1,
    vendor_id              integer,
    industry_oid           TEXT,
    organization_guid      TEXT
);

drop table if exists refdata_codeset;
CREATE TABLE refdata_codeset
(
    codesets_id        integer primary key autoincrement,
    codeset_name       TEXT,
    industry_std       TEXT,
    status_id          integer   DEFAULT 1,
    created_date       TEXT default (datetime('now', 'localtime')),
    created_user       TEXT,
    codeset_guid       TEXT,
    field_mapping      TEXT,
    sensitivityflag_id integer,
    externaltable_id   TEXT,
    external_notes     TEXT,
    external_link      TEXT
);

drop table if exists refdata_countries;
CREATE TABLE refdata_countries
(
    country_id   integer primary key autoincrement,
    idd          TEXT,
    country_name TEXT,
    created_date TEXT default (datetime('now', 'localtime')),
    status_id    integer   DEFAULT 1
);

drop table if exists refdata_devicetypes;
CREATE TABLE refdata_devicetypes
(
    devicetype_id integer primary key autoincrement,
    devicetype    TEXT,
    created_date  TEXT default (datetime('now', 'localtime')),
    status_id     integer   DEFAULT 1
);

drop table if exists refdata_industrystd_eventtypes;
CREATE TABLE refdata_industrystd_eventtypes
(
    eventtype_id   TEXT NOT NULL,
    eventtype_desc TEXT,
    industry_std   TEXT(6),
    created_date   TEXT default (datetime('now', 'localtime')),
    status_id      integer   default 1
);

drop table if exists refdata_industries;
CREATE TABLE refdata_industries
(
    industry_id   integer primary key autoincrement ,
    industry_name TEXT(45),
    created_date  TEXT default (datetime('now', 'localtime')),
    status_id     integer   DEFAULT 1
);

drop table if exists refdata_industriestobusiness;
CREATE TABLE refdata_industriestobusiness
(
    industrytobusiness_id integer primary key autoincrement,
    industry_id           integer,
    business_area         TEXT,
    created_date          TEXT default (datetime('now', 'localtime')),
    status_id             integer   DEFAULT 1
);

drop table if exists refdata_industrystd;
CREATE TABLE refdata_industrystd
(
    industry_std     TEXT primary key,
    industrystd_desc TEXT,
    created_date     TEXT default (datetime('now', 'localtime')),
    status_id        integer   DEFAULT 1
);

drop table if exists refdata_legalentities;
CREATE TABLE refdata_legalentities
(
    legalentity_guid TEXT  primary key,
    location_name    TEXT,
    address          TEXT,
    city             TEXT,
    state_id         TEXT,
    zipcode          TEXT,
    created_user     TEXT,
    status_id        integer   DEFAULT 1,
    created_date     TEXT default (datetime('now', 'localtime')),
    location_url     TEXT,
    location_phone   TEXT
);

drop table if exists refdata_operationtype;
CREATE TABLE refdata_operationtype
(
    operationtype_id   TEXT primary key,
    operationtype_name TEXT,
    created_date       TEXT default (datetime('now', 'localtime')),
    status_id          integer   DEFAULT 1
);

drop table if exists refdata_organization;
CREATE TABLE refdata_organization
(
    organization_guid          TEXT primary key,
    organization_internal_code TEXT,
    organization_internal_id   TEXT,
    organization_name          TEXT,
    address                    TEXT,
    city                       TEXT,
    state_id                   TEXT,
    zipcode                    TEXT,
    created_user               TEXT,
    status_id                  integer   DEFAULT 1,
    created_date               TEXT default (datetime('now', 'localtime')),
    legalentity_guid           TEXT
);

drop table if exists refdata_regextypes;
CREATE TABLE refdata_regextypes
(
    regextype_id      integer  primary key autoincrement,
    regextype_desc    TEXT,
    created_date      TEXT default (datetime('now', 'localtime')),
    status_id         integer   DEFAULT 1,
    organization_guid TEXT,
    application_guid  TEXT
);

drop table if exists refdata_rulesets;
CREATE TABLE refdata_rulesets
(
    rule_id         integer  primary key autoincrement,
    rule_name       TEXT(65),
    created_user    TEXT,
    created_date    TEXT default (datetime('now', 'localtime')),
    status_id       integer   DEFAULT 1,
    expiration_date TEXT
);

drop table if exists refdata_rulesetsdefinitions;
CREATE TABLE refdata_rulesetsdefinitions
(
    rulesetdefinitions_id   TEXT NOT NULL,
    rulesetdefinitions_name TEXT,
    ruleset_id              integer,
    steporder_id            integer,
    operationtype_id        TEXT,
    ruleset_defvalue        char,
    status_id               integer   DEFAULT 1,
    created_date            TEXT default (datetime('now', 'localtime')),
    effective_date          TEXT,
    application_guid        TEXT,
    term_date               TEXT,
    dataattribute_id        integer
);

drop table if exists refdata_professiontypes;
CREATE TABLE refdata_professiontypes
(
    professiontype_id   integer primary key autoincrement,
    professiontype_name TEXT(65),
    created_user        TEXT,
    created_date        TEXT default (datetime('now', 'localtime')),
    status_id           integer   DEFAULT 1
);

drop table if exists refdata_sensitivityflag;
CREATE TABLE refdata_sensitivityflag
(
    sensitiveflag_id   integer primary key autoincrement,
    sensitiveflag_desc TEXT,
    created_date       TEXT default (datetime('now', 'localtime')),
    status_id          integer   DEFAULT 1
);

drop table if exists refdata_status;
CREATE TABLE refdata_status
(
    status_id          integer primary key autoincrement,
    status_description TEXT(45)                                                 NOT NULL,
    created_date       TEXT default (datetime('now', 'localtime')),
    created_user       TEXT
);

drop table if exists refdata_terminologystd;
CREATE TABLE refdata_terminologystd
(
    terminologystd_id      integer primary key autoincrement,
    terminologystd         TEXT(25)                                                          NOT NULL,
    terminologystd_version TEXT                                                              NOT NULL,
    terminologystd_desc    TEXT,
    created_date           TEXT default (datetime('now', 'localtime')),
    status_id              integer   DEFAULT 1
);

drop table if exists refdata_timezones;
CREATE TABLE refdata_timezones
(
    timezone_value TEXT(3) primary key,
    timezone_desc  TEXT(25),
    created_date   TEXT default (datetime('now', 'localtime')),
    status_id      integer   DEFAULT 1
);

drop table if exists refdata_usstates;
CREATE TABLE refdata_usstates
(
    state_id          TEXT primary key,
    state_description TEXT(65),
    lattitude         TEXT,
    longitude         TEXT,
    created_date      TEXT default (datetime('now', 'localtime')),
    status_id         integer   DEFAULT 1,
    created_user      TEXT
);

drop table if exists refdata_vendor;
CREATE TABLE refdata_vendor
(
    vendor_id    integer   primary key autoincrement,
    vendor_name  TEXT,
    created_date TEXT default (datetime('now', 'localtime')),
    status_id    integer   DEFAULT 1,
    created_user TEXT,
    vendor_guid  TEXT
);

drop table if exists terms_codeset_industrystd;
CREATE TABLE terms_codeset_industrystd
(
    termcodeset_id    integer  primary key autoincrement,
    codesets_id       integer                                                              NOT NULL,
    created_date      TEXT default (datetime('now', 'localtime')),
    status_id         integer   DEFAULT 1,
    code_value        TEXT,
    code_desc         TEXT,
    industry_std      TEXT,
    terminologystd_id integer
);

-- Indexes
create index if not exists datatiersdp_dataattributes_index
    on datatier_sdp_dataattributes (datatier_id, basevalue, supportingvalue1, supportingvalue2, supportingvalue3, supportingvalue4,
    supportingvalue5, supportingvalue6, supportingvalue7, created_date, dataattribute_id,
    datagentype_id, status_id, created_user, registeredapp_guid);

CREATE INDEX terms_codeset_industrystd_index ON terms_codeset_industrystd(termcodeset_id, codesets_id, created_date, status_id, code_value, code_desc, industry_std);

CREATE UNIQUE INDEX terms_codeset_industrystd_uindex ON terms_codeset_industrystd(codesets_id, code_value, code_desc, industry_std);
