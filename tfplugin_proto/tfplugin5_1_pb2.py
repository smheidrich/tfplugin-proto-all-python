from typing import Any
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tfplugin5_1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11tfplugin5_1.proto\x12\ttfplugin5\"-\n\x0c\x44ynamicValue\x12\x0f\n\x07msgpack\x18\x01 \x01(\x0c\x12\x0c\n\x04json\x18\x02 \x01(\x0c\"\xbd\x01\n\nDiagnostic\x12\x30\n\x08severity\x18\x01 \x01(\x0e\x32\x1e.tfplugin5.Diagnostic.Severity\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\x12+\n\tattribute\x18\x04 \x01(\x0b\x32\x18.tfplugin5.AttributePath\"/\n\x08Severity\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0b\n\x07WARNING\x10\x02\"\xa4\x01\n\rAttributePath\x12,\n\x05steps\x18\x01 \x03(\x0b\x32\x1d.tfplugin5.AttributePath.Step\x1a\x65\n\x04Step\x12\x18\n\x0e\x61ttribute_name\x18\x01 \x01(\tH\x00\x12\x1c\n\x12\x65lement_key_string\x18\x02 \x01(\tH\x00\x12\x19\n\x0f\x65lement_key_int\x18\x03 \x01(\x03H\x00\x42\n\n\x08selector\",\n\x04Stop\x1a\t\n\x07Request\x1a\x19\n\x08Response\x12\r\n\x05\x45rror\x18\x01 \x01(\t\"{\n\x08RawState\x12\x0c\n\x04json\x18\x01 \x01(\x0c\x12\x31\n\x07\x66latmap\x18\x02 \x03(\x0b\x32 .tfplugin5.RawState.FlatmapEntry\x1a.\n\x0c\x46latmapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc4\x04\n\x06Schema\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tfplugin5.Schema.Block\x1a}\n\x05\x42lock\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12/\n\nattributes\x18\x02 \x03(\x0b\x32\x1b.tfplugin5.Schema.Attribute\x12\x32\n\x0b\x62lock_types\x18\x03 \x03(\x0b\x32\x1d.tfplugin5.Schema.NestedBlock\x1a\x85\x01\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x0c\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08required\x18\x04 \x01(\x08\x12\x10\n\x08optional\x18\x05 \x01(\x08\x12\x10\n\x08\x63omputed\x18\x06 \x01(\x08\x12\x11\n\tsensitive\x18\x07 \x01(\x08\x1a\xf9\x01\n\x0bNestedBlock\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tfplugin5.Schema.Block\x12:\n\x07nesting\x18\x03 \x01(\x0e\x32).tfplugin5.Schema.NestedBlock.NestingMode\x12\x11\n\tmin_items\x18\x04 \x01(\x03\x12\x11\n\tmax_items\x18\x05 \x01(\x03\"M\n\x0bNestingMode\x12\x0b\n\x07INVALID\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\x08\n\x04LIST\x10\x02\x12\x07\n\x03SET\x10\x03\x12\x07\n\x03MAP\x10\x04\x12\t\n\x05GROUP\x10\x05\"\xc5\x03\n\x11GetProviderSchema\x1a\t\n\x07Request\x1a\xa4\x03\n\x08Response\x12#\n\x08provider\x18\x01 \x01(\x0b\x32\x11.tfplugin5.Schema\x12T\n\x10resource_schemas\x18\x02 \x03(\x0b\x32:.tfplugin5.GetProviderSchema.Response.ResourceSchemasEntry\x12Y\n\x13\x64\x61ta_source_schemas\x18\x03 \x03(\x0b\x32<.tfplugin5.GetProviderSchema.Response.DataSourceSchemasEntry\x12*\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x1aI\n\x14ResourceSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.tfplugin5.Schema:\x02\x38\x01\x1aK\n\x16\x44\x61taSourceSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.tfplugin5.Schema:\x02\x38\x01\"\xb5\x01\n\x15PrepareProviderConfig\x1a\x32\n\x07Request\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1ah\n\x08Response\x12\x30\n\x0fprepared_config\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\xd6\x01\n\x14UpgradeResourceState\x1aU\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12&\n\traw_state\x18\x03 \x01(\x0b\x32\x13.tfplugin5.RawState\x1ag\n\x08Response\x12/\n\x0eupgraded_state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x9b\x01\n\x1aValidateResourceTypeConfig\x1a\x45\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x99\x01\n\x18ValidateDataSourceConfig\x1a\x45\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x92\x01\n\tConfigure\x1aM\n\x07Request\x12\x19\n\x11terraform_version\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\xe2\x01\n\x0cReadResource\x1a]\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12.\n\rcurrent_state\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x1as\n\x08Response\x12*\n\tnew_state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x12\x0f\n\x07private\x18\x03 \x01(\x0c\"\xa8\x03\n\x12PlanResourceChange\x1a\xbf\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12,\n\x0bprior_state\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x33\n\x12proposed_new_state\x18\x03 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\'\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x15\n\rprior_private\x18\x05 \x01(\x0c\x1a\xcf\x01\n\x08Response\x12.\n\rplanned_state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x32\n\x10requires_replace\x18\x02 \x03(\x0b\x32\x18.tfplugin5.AttributePath\x12\x17\n\x0fplanned_private\x18\x03 \x01(\x0c\x12*\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x12\x1a\n\x12legacy_type_system\x18\x05 \x01(\x08\"\xe6\x02\n\x13\x41pplyResourceChange\x1a\xbc\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12,\n\x0bprior_state\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12.\n\rplanned_state\x18\x03 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\'\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x17\n\x0fplanned_private\x18\x05 \x01(\x0c\x1a\x8f\x01\n\x08Response\x12*\n\tnew_state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x0f\n\x07private\x18\x02 \x01(\x0c\x12*\n\x0b\x64iagnostics\x18\x03 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x12\x1a\n\x12legacy_type_system\x18\x04 \x01(\x08\"\xa5\x02\n\x13ImportResourceState\x1a(\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x1a^\n\x10ImportedResource\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12&\n\x05state\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x1a\x83\x01\n\x08Response\x12K\n\x12imported_resources\x18\x01 \x03(\x0b\x32/.tfplugin5.ImportResourceState.ImportedResource\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\xb7\x01\n\x0eReadDataSource\x1a\x45\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a^\n\x08Response\x12&\n\x05state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x81\x01\n\x14GetProvisionerSchema\x1a\t\n\x07Request\x1a^\n\x08Response\x12&\n\x0bprovisioner\x18\x01 \x01(\x0b\x32\x11.tfplugin5.Schema\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x87\x01\n\x19ValidateProvisionerConfig\x1a\x32\n\x07Request\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\xbc\x01\n\x11ProvisionResource\x1a_\n\x07Request\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12+\n\nconnection\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x46\n\x08Response\x12\x0e\n\x06output\x18\x01 \x01(\t\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic2\x97\t\n\x08Provider\x12X\n\tGetSchema\x12$.tfplugin5.GetProviderSchema.Request\x1a%.tfplugin5.GetProviderSchema.Response\x12l\n\x15PrepareProviderConfig\x12(.tfplugin5.PrepareProviderConfig.Request\x1a).tfplugin5.PrepareProviderConfig.Response\x12{\n\x1aValidateResourceTypeConfig\x12-.tfplugin5.ValidateResourceTypeConfig.Request\x1a..tfplugin5.ValidateResourceTypeConfig.Response\x12u\n\x18ValidateDataSourceConfig\x12+.tfplugin5.ValidateDataSourceConfig.Request\x1a,.tfplugin5.ValidateDataSourceConfig.Response\x12i\n\x14UpgradeResourceState\x12\'.tfplugin5.UpgradeResourceState.Request\x1a(.tfplugin5.UpgradeResourceState.Response\x12H\n\tConfigure\x12\x1c.tfplugin5.Configure.Request\x1a\x1d.tfplugin5.Configure.Response\x12Q\n\x0cReadResource\x12\x1f.tfplugin5.ReadResource.Request\x1a .tfplugin5.ReadResource.Response\x12\x63\n\x12PlanResourceChange\x12%.tfplugin5.PlanResourceChange.Request\x1a&.tfplugin5.PlanResourceChange.Response\x12\x66\n\x13\x41pplyResourceChange\x12&.tfplugin5.ApplyResourceChange.Request\x1a\'.tfplugin5.ApplyResourceChange.Response\x12\x66\n\x13ImportResourceState\x12&.tfplugin5.ImportResourceState.Request\x1a\'.tfplugin5.ImportResourceState.Response\x12W\n\x0eReadDataSource\x12!.tfplugin5.ReadDataSource.Request\x1a\".tfplugin5.ReadDataSource.Response\x12\x39\n\x04Stop\x12\x17.tfplugin5.Stop.Request\x1a\x18.tfplugin5.Stop.Response2\x86\x03\n\x0bProvisioner\x12^\n\tGetSchema\x12\'.tfplugin5.GetProvisionerSchema.Request\x1a(.tfplugin5.GetProvisionerSchema.Response\x12x\n\x19ValidateProvisionerConfig\x12,.tfplugin5.ValidateProvisionerConfig.Request\x1a-.tfplugin5.ValidateProvisionerConfig.Response\x12\x62\n\x11ProvisionResource\x12$.tfplugin5.ProvisionResource.Request\x1a%.tfplugin5.ProvisionResource.Response0\x01\x12\x39\n\x04Stop\x12\x17.tfplugin5.Stop.Request\x1a\x18.tfplugin5.Stop.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tfplugin5_1_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _RAWSTATE_FLATMAPENTRY._options = None
  _RAWSTATE_FLATMAPENTRY._serialized_options = b'8\001'
  _GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY._options = None
  _GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY._serialized_options = b'8\001'
  _GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY._options = None
  _GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY._serialized_options = b'8\001'
  _globals['_DYNAMICVALUE']._serialized_start=32
  _globals['_DYNAMICVALUE']._serialized_end=77
  _globals['_DIAGNOSTIC']._serialized_start=80
  _globals['_DIAGNOSTIC']._serialized_end=269
  _globals['_DIAGNOSTIC_SEVERITY']._serialized_start=222
  _globals['_DIAGNOSTIC_SEVERITY']._serialized_end=269
  _globals['_ATTRIBUTEPATH']._serialized_start=272
  _globals['_ATTRIBUTEPATH']._serialized_end=436
  _globals['_ATTRIBUTEPATH_STEP']._serialized_start=335
  _globals['_ATTRIBUTEPATH_STEP']._serialized_end=436
  _globals['_STOP']._serialized_start=438
  _globals['_STOP']._serialized_end=482
  _globals['_STOP_REQUEST']._serialized_start=446
  _globals['_STOP_REQUEST']._serialized_end=455
  _globals['_STOP_RESPONSE']._serialized_start=457
  _globals['_STOP_RESPONSE']._serialized_end=482
  _globals['_RAWSTATE']._serialized_start=484
  _globals['_RAWSTATE']._serialized_end=607
  _globals['_RAWSTATE_FLATMAPENTRY']._serialized_start=561
  _globals['_RAWSTATE_FLATMAPENTRY']._serialized_end=607
  _globals['_SCHEMA']._serialized_start=610
  _globals['_SCHEMA']._serialized_end=1190
  _globals['_SCHEMA_BLOCK']._serialized_start=677
  _globals['_SCHEMA_BLOCK']._serialized_end=802
  _globals['_SCHEMA_ATTRIBUTE']._serialized_start=805
  _globals['_SCHEMA_ATTRIBUTE']._serialized_end=938
  _globals['_SCHEMA_NESTEDBLOCK']._serialized_start=941
  _globals['_SCHEMA_NESTEDBLOCK']._serialized_end=1190
  _globals['_SCHEMA_NESTEDBLOCK_NESTINGMODE']._serialized_start=1113
  _globals['_SCHEMA_NESTEDBLOCK_NESTINGMODE']._serialized_end=1190
  _globals['_GETPROVIDERSCHEMA']._serialized_start=1193
  _globals['_GETPROVIDERSCHEMA']._serialized_end=1646
  _globals['_GETPROVIDERSCHEMA_REQUEST']._serialized_start=446
  _globals['_GETPROVIDERSCHEMA_REQUEST']._serialized_end=455
  _globals['_GETPROVIDERSCHEMA_RESPONSE']._serialized_start=1226
  _globals['_GETPROVIDERSCHEMA_RESPONSE']._serialized_end=1646
  _globals['_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY']._serialized_start=1496
  _globals['_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY']._serialized_end=1569
  _globals['_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY']._serialized_start=1571
  _globals['_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY']._serialized_end=1646
  _globals['_PREPAREPROVIDERCONFIG']._serialized_start=1649
  _globals['_PREPAREPROVIDERCONFIG']._serialized_end=1830
  _globals['_PREPAREPROVIDERCONFIG_REQUEST']._serialized_start=1674
  _globals['_PREPAREPROVIDERCONFIG_REQUEST']._serialized_end=1724
  _globals['_PREPAREPROVIDERCONFIG_RESPONSE']._serialized_start=1726
  _globals['_PREPAREPROVIDERCONFIG_RESPONSE']._serialized_end=1830
  _globals['_UPGRADERESOURCESTATE']._serialized_start=1833
  _globals['_UPGRADERESOURCESTATE']._serialized_end=2047
  _globals['_UPGRADERESOURCESTATE_REQUEST']._serialized_start=1857
  _globals['_UPGRADERESOURCESTATE_REQUEST']._serialized_end=1942
  _globals['_UPGRADERESOURCESTATE_RESPONSE']._serialized_start=1944
  _globals['_UPGRADERESOURCESTATE_RESPONSE']._serialized_end=2047
  _globals['_VALIDATERESOURCETYPECONFIG']._serialized_start=2050
  _globals['_VALIDATERESOURCETYPECONFIG']._serialized_end=2205
  _globals['_VALIDATERESOURCETYPECONFIG_REQUEST']._serialized_start=2080
  _globals['_VALIDATERESOURCETYPECONFIG_REQUEST']._serialized_end=2149
  _globals['_VALIDATERESOURCETYPECONFIG_RESPONSE']._serialized_start=2151
  _globals['_VALIDATERESOURCETYPECONFIG_RESPONSE']._serialized_end=2205
  _globals['_VALIDATEDATASOURCECONFIG']._serialized_start=2208
  _globals['_VALIDATEDATASOURCECONFIG']._serialized_end=2361
  _globals['_VALIDATEDATASOURCECONFIG_REQUEST']._serialized_start=2080
  _globals['_VALIDATEDATASOURCECONFIG_REQUEST']._serialized_end=2149
  _globals['_VALIDATEDATASOURCECONFIG_RESPONSE']._serialized_start=2151
  _globals['_VALIDATEDATASOURCECONFIG_RESPONSE']._serialized_end=2205
  _globals['_CONFIGURE']._serialized_start=2364
  _globals['_CONFIGURE']._serialized_end=2510
  _globals['_CONFIGURE_REQUEST']._serialized_start=2377
  _globals['_CONFIGURE_REQUEST']._serialized_end=2454
  _globals['_CONFIGURE_RESPONSE']._serialized_start=2151
  _globals['_CONFIGURE_RESPONSE']._serialized_end=2205
  _globals['_READRESOURCE']._serialized_start=2513
  _globals['_READRESOURCE']._serialized_end=2739
  _globals['_READRESOURCE_REQUEST']._serialized_start=2529
  _globals['_READRESOURCE_REQUEST']._serialized_end=2622
  _globals['_READRESOURCE_RESPONSE']._serialized_start=2624
  _globals['_READRESOURCE_RESPONSE']._serialized_end=2739
  _globals['_PLANRESOURCECHANGE']._serialized_start=2742
  _globals['_PLANRESOURCECHANGE']._serialized_end=3166
  _globals['_PLANRESOURCECHANGE_REQUEST']._serialized_start=2765
  _globals['_PLANRESOURCECHANGE_REQUEST']._serialized_end=2956
  _globals['_PLANRESOURCECHANGE_RESPONSE']._serialized_start=2959
  _globals['_PLANRESOURCECHANGE_RESPONSE']._serialized_end=3166
  _globals['_APPLYRESOURCECHANGE']._serialized_start=3169
  _globals['_APPLYRESOURCECHANGE']._serialized_end=3527
  _globals['_APPLYRESOURCECHANGE_REQUEST']._serialized_start=3193
  _globals['_APPLYRESOURCECHANGE_REQUEST']._serialized_end=3381
  _globals['_APPLYRESOURCECHANGE_RESPONSE']._serialized_start=3384
  _globals['_APPLYRESOURCECHANGE_RESPONSE']._serialized_end=3527
  _globals['_IMPORTRESOURCESTATE']._serialized_start=3530
  _globals['_IMPORTRESOURCESTATE']._serialized_end=3823
  _globals['_IMPORTRESOURCESTATE_REQUEST']._serialized_start=3553
  _globals['_IMPORTRESOURCESTATE_REQUEST']._serialized_end=3593
  _globals['_IMPORTRESOURCESTATE_IMPORTEDRESOURCE']._serialized_start=3595
  _globals['_IMPORTRESOURCESTATE_IMPORTEDRESOURCE']._serialized_end=3689
  _globals['_IMPORTRESOURCESTATE_RESPONSE']._serialized_start=3692
  _globals['_IMPORTRESOURCESTATE_RESPONSE']._serialized_end=3823
  _globals['_READDATASOURCE']._serialized_start=3826
  _globals['_READDATASOURCE']._serialized_end=4009
  _globals['_READDATASOURCE_REQUEST']._serialized_start=2080
  _globals['_READDATASOURCE_REQUEST']._serialized_end=2149
  _globals['_READDATASOURCE_RESPONSE']._serialized_start=3915
  _globals['_READDATASOURCE_RESPONSE']._serialized_end=4009
  _globals['_GETPROVISIONERSCHEMA']._serialized_start=4012
  _globals['_GETPROVISIONERSCHEMA']._serialized_end=4141
  _globals['_GETPROVISIONERSCHEMA_REQUEST']._serialized_start=446
  _globals['_GETPROVISIONERSCHEMA_REQUEST']._serialized_end=455
  _globals['_GETPROVISIONERSCHEMA_RESPONSE']._serialized_start=4047
  _globals['_GETPROVISIONERSCHEMA_RESPONSE']._serialized_end=4141
  _globals['_VALIDATEPROVISIONERCONFIG']._serialized_start=4144
  _globals['_VALIDATEPROVISIONERCONFIG']._serialized_end=4279
  _globals['_VALIDATEPROVISIONERCONFIG_REQUEST']._serialized_start=1674
  _globals['_VALIDATEPROVISIONERCONFIG_REQUEST']._serialized_end=1724
  _globals['_VALIDATEPROVISIONERCONFIG_RESPONSE']._serialized_start=2151
  _globals['_VALIDATEPROVISIONERCONFIG_RESPONSE']._serialized_end=2205
  _globals['_PROVISIONRESOURCE']._serialized_start=4282
  _globals['_PROVISIONRESOURCE']._serialized_end=4470
  _globals['_PROVISIONRESOURCE_REQUEST']._serialized_start=4303
  _globals['_PROVISIONRESOURCE_REQUEST']._serialized_end=4398
  _globals['_PROVISIONRESOURCE_RESPONSE']._serialized_start=4400
  _globals['_PROVISIONRESOURCE_RESPONSE']._serialized_end=4470
  _globals['_PROVIDER']._serialized_start=4473
  _globals['_PROVIDER']._serialized_end=5648
  _globals['_PROVISIONER']._serialized_start=5651
  _globals['_PROVISIONER']._serialized_end=6041
# @@protoc_insertion_point(module_scope)
