from typing import Any
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tfplugin5_3.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11tfplugin5_3.proto\x12\ttfplugin5\"-\n\x0c\x44ynamicValue\x12\x0f\n\x07msgpack\x18\x01 \x01(\x0c\x12\x0c\n\x04json\x18\x02 \x01(\x0c\"\xbd\x01\n\nDiagnostic\x12\x30\n\x08severity\x18\x01 \x01(\x0e\x32\x1e.tfplugin5.Diagnostic.Severity\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\x12+\n\tattribute\x18\x04 \x01(\x0b\x32\x18.tfplugin5.AttributePath\"/\n\x08Severity\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0b\n\x07WARNING\x10\x02\"\xa4\x01\n\rAttributePath\x12,\n\x05steps\x18\x01 \x03(\x0b\x32\x1d.tfplugin5.AttributePath.Step\x1a\x65\n\x04Step\x12\x18\n\x0e\x61ttribute_name\x18\x01 \x01(\tH\x00\x12\x1c\n\x12\x65lement_key_string\x18\x02 \x01(\tH\x00\x12\x19\n\x0f\x65lement_key_int\x18\x03 \x01(\x03H\x00\x42\n\n\x08selector\",\n\x04Stop\x1a\t\n\x07Request\x1a\x19\n\x08Response\x12\r\n\x05\x45rror\x18\x01 \x01(\t\"{\n\x08RawState\x12\x0c\n\x04json\x18\x01 \x01(\x0c\x12\x31\n\x07\x66latmap\x18\x02 \x03(\x0b\x32 .tfplugin5.RawState.FlatmapEntry\x1a.\n\x0c\x46latmapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe4\x05\n\x06Schema\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tfplugin5.Schema.Block\x1a\xd7\x01\n\x05\x42lock\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12/\n\nattributes\x18\x02 \x03(\x0b\x32\x1b.tfplugin5.Schema.Attribute\x12\x32\n\x0b\x62lock_types\x18\x03 \x03(\x0b\x32\x1d.tfplugin5.Schema.NestedBlock\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12/\n\x10\x64\x65scription_kind\x18\x05 \x01(\x0e\x32\x15.tfplugin5.StringKind\x12\x12\n\ndeprecated\x18\x06 \x01(\x08\x1a\xca\x01\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x0c\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08required\x18\x04 \x01(\x08\x12\x10\n\x08optional\x18\x05 \x01(\x08\x12\x10\n\x08\x63omputed\x18\x06 \x01(\x08\x12\x11\n\tsensitive\x18\x07 \x01(\x08\x12/\n\x10\x64\x65scription_kind\x18\x08 \x01(\x0e\x32\x15.tfplugin5.StringKind\x12\x12\n\ndeprecated\x18\t \x01(\x08\x1a\xf9\x01\n\x0bNestedBlock\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tfplugin5.Schema.Block\x12:\n\x07nesting\x18\x03 \x01(\x0e\x32).tfplugin5.Schema.NestedBlock.NestingMode\x12\x11\n\tmin_items\x18\x04 \x01(\x03\x12\x11\n\tmax_items\x18\x05 \x01(\x03\"M\n\x0bNestingMode\x12\x0b\n\x07INVALID\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\x08\n\x04LIST\x10\x02\x12\x07\n\x03SET\x10\x03\x12\x07\n\x03MAP\x10\x04\x12\t\n\x05GROUP\x10\x05\"\xe9\x04\n\x11GetProviderSchema\x1a\t\n\x07Request\x1a\x9c\x04\n\x08Response\x12#\n\x08provider\x18\x01 \x01(\x0b\x32\x11.tfplugin5.Schema\x12T\n\x10resource_schemas\x18\x02 \x03(\x0b\x32:.tfplugin5.GetProviderSchema.Response.ResourceSchemasEntry\x12Y\n\x13\x64\x61ta_source_schemas\x18\x03 \x03(\x0b\x32<.tfplugin5.GetProviderSchema.Response.DataSourceSchemasEntry\x12*\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x12(\n\rprovider_meta\x18\x05 \x01(\x0b\x32\x11.tfplugin5.Schema\x12L\n\x13server_capabilities\x18\x06 \x01(\x0b\x32/.tfplugin5.GetProviderSchema.ServerCapabilities\x1aI\n\x14ResourceSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.tfplugin5.Schema:\x02\x38\x01\x1aK\n\x16\x44\x61taSourceSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.tfplugin5.Schema:\x02\x38\x01\x1a*\n\x12ServerCapabilities\x12\x14\n\x0cplan_destroy\x18\x01 \x01(\x08\"\xb5\x01\n\x15PrepareProviderConfig\x1a\x32\n\x07Request\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1ah\n\x08Response\x12\x30\n\x0fprepared_config\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\xd6\x01\n\x14UpgradeResourceState\x1aU\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12&\n\traw_state\x18\x03 \x01(\x0b\x32\x13.tfplugin5.RawState\x1ag\n\x08Response\x12/\n\x0eupgraded_state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x9b\x01\n\x1aValidateResourceTypeConfig\x1a\x45\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x99\x01\n\x18ValidateDataSourceConfig\x1a\x45\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x92\x01\n\tConfigure\x1aM\n\x07Request\x12\x19\n\x11terraform_version\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x93\x02\n\x0cReadResource\x1a\x8d\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12.\n\rcurrent_state\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x12.\n\rprovider_meta\x18\x04 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1as\n\x08Response\x12*\n\tnew_state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x12\x0f\n\x07private\x18\x03 \x01(\x0c\"\xd8\x03\n\x12PlanResourceChange\x1a\xef\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12,\n\x0bprior_state\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x33\n\x12proposed_new_state\x18\x03 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\'\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x15\n\rprior_private\x18\x05 \x01(\x0c\x12.\n\rprovider_meta\x18\x06 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\xcf\x01\n\x08Response\x12.\n\rplanned_state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x32\n\x10requires_replace\x18\x02 \x03(\x0b\x32\x18.tfplugin5.AttributePath\x12\x17\n\x0fplanned_private\x18\x03 \x01(\x0c\x12*\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x12\x1a\n\x12legacy_type_system\x18\x05 \x01(\x08\"\x96\x03\n\x13\x41pplyResourceChange\x1a\xec\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12,\n\x0bprior_state\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12.\n\rplanned_state\x18\x03 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\'\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x17\n\x0fplanned_private\x18\x05 \x01(\x0c\x12.\n\rprovider_meta\x18\x06 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x8f\x01\n\x08Response\x12*\n\tnew_state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x0f\n\x07private\x18\x02 \x01(\x0c\x12*\n\x0b\x64iagnostics\x18\x03 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x12\x1a\n\x12legacy_type_system\x18\x04 \x01(\x08\"\xa5\x02\n\x13ImportResourceState\x1a(\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x1a^\n\x10ImportedResource\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12&\n\x05state\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x1a\x83\x01\n\x08Response\x12K\n\x12imported_resources\x18\x01 \x03(\x0b\x32/.tfplugin5.ImportResourceState.ImportedResource\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\xe7\x01\n\x0eReadDataSource\x1au\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12.\n\rprovider_meta\x18\x03 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a^\n\x08Response\x12&\n\x05state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x81\x01\n\x14GetProvisionerSchema\x1a\t\n\x07Request\x1a^\n\x08Response\x12&\n\x0bprovisioner\x18\x01 \x01(\x0b\x32\x11.tfplugin5.Schema\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x87\x01\n\x19ValidateProvisionerConfig\x1a\x32\n\x07Request\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\xbc\x01\n\x11ProvisionResource\x1a_\n\x07Request\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12+\n\nconnection\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x46\n\x08Response\x12\x0e\n\x06output\x18\x01 \x01(\t\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic*%\n\nStringKind\x12\t\n\x05PLAIN\x10\x00\x12\x0c\n\x08MARKDOWN\x10\x01\x32\x97\t\n\x08Provider\x12X\n\tGetSchema\x12$.tfplugin5.GetProviderSchema.Request\x1a%.tfplugin5.GetProviderSchema.Response\x12l\n\x15PrepareProviderConfig\x12(.tfplugin5.PrepareProviderConfig.Request\x1a).tfplugin5.PrepareProviderConfig.Response\x12{\n\x1aValidateResourceTypeConfig\x12-.tfplugin5.ValidateResourceTypeConfig.Request\x1a..tfplugin5.ValidateResourceTypeConfig.Response\x12u\n\x18ValidateDataSourceConfig\x12+.tfplugin5.ValidateDataSourceConfig.Request\x1a,.tfplugin5.ValidateDataSourceConfig.Response\x12i\n\x14UpgradeResourceState\x12\'.tfplugin5.UpgradeResourceState.Request\x1a(.tfplugin5.UpgradeResourceState.Response\x12H\n\tConfigure\x12\x1c.tfplugin5.Configure.Request\x1a\x1d.tfplugin5.Configure.Response\x12Q\n\x0cReadResource\x12\x1f.tfplugin5.ReadResource.Request\x1a .tfplugin5.ReadResource.Response\x12\x63\n\x12PlanResourceChange\x12%.tfplugin5.PlanResourceChange.Request\x1a&.tfplugin5.PlanResourceChange.Response\x12\x66\n\x13\x41pplyResourceChange\x12&.tfplugin5.ApplyResourceChange.Request\x1a\'.tfplugin5.ApplyResourceChange.Response\x12\x66\n\x13ImportResourceState\x12&.tfplugin5.ImportResourceState.Request\x1a\'.tfplugin5.ImportResourceState.Response\x12W\n\x0eReadDataSource\x12!.tfplugin5.ReadDataSource.Request\x1a\".tfplugin5.ReadDataSource.Response\x12\x39\n\x04Stop\x12\x17.tfplugin5.Stop.Request\x1a\x18.tfplugin5.Stop.Response2\x86\x03\n\x0bProvisioner\x12^\n\tGetSchema\x12\'.tfplugin5.GetProvisionerSchema.Request\x1a(.tfplugin5.GetProvisionerSchema.Response\x12x\n\x19ValidateProvisionerConfig\x12,.tfplugin5.ValidateProvisionerConfig.Request\x1a-.tfplugin5.ValidateProvisionerConfig.Response\x12\x62\n\x11ProvisionResource\x12$.tfplugin5.ProvisionResource.Request\x1a%.tfplugin5.ProvisionResource.Response0\x01\x12\x39\n\x04Stop\x12\x17.tfplugin5.Stop.Request\x1a\x18.tfplugin5.Stop.ResponseB3Z1github.com/hashicorp/terraform/internal/tfplugin5b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tfplugin5_3_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/hashicorp/terraform/internal/tfplugin5'
  _RAWSTATE_FLATMAPENTRY._options = None
  _RAWSTATE_FLATMAPENTRY._serialized_options = b'8\001'
  _GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY._options = None
  _GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY._serialized_options = b'8\001'
  _GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY._options = None
  _GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY._serialized_options = b'8\001'
  _globals['_STRINGKIND']._serialized_start=4989
  _globals['_STRINGKIND']._serialized_end=5026
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
  _globals['_SCHEMA']._serialized_end=1350
  _globals['_SCHEMA_BLOCK']._serialized_start=678
  _globals['_SCHEMA_BLOCK']._serialized_end=893
  _globals['_SCHEMA_ATTRIBUTE']._serialized_start=896
  _globals['_SCHEMA_ATTRIBUTE']._serialized_end=1098
  _globals['_SCHEMA_NESTEDBLOCK']._serialized_start=1101
  _globals['_SCHEMA_NESTEDBLOCK']._serialized_end=1350
  _globals['_SCHEMA_NESTEDBLOCK_NESTINGMODE']._serialized_start=1273
  _globals['_SCHEMA_NESTEDBLOCK_NESTINGMODE']._serialized_end=1350
  _globals['_GETPROVIDERSCHEMA']._serialized_start=1353
  _globals['_GETPROVIDERSCHEMA']._serialized_end=1970
  _globals['_GETPROVIDERSCHEMA_REQUEST']._serialized_start=446
  _globals['_GETPROVIDERSCHEMA_REQUEST']._serialized_end=455
  _globals['_GETPROVIDERSCHEMA_RESPONSE']._serialized_start=1386
  _globals['_GETPROVIDERSCHEMA_RESPONSE']._serialized_end=1926
  _globals['_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY']._serialized_start=1776
  _globals['_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY']._serialized_end=1849
  _globals['_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY']._serialized_start=1851
  _globals['_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY']._serialized_end=1926
  _globals['_GETPROVIDERSCHEMA_SERVERCAPABILITIES']._serialized_start=1928
  _globals['_GETPROVIDERSCHEMA_SERVERCAPABILITIES']._serialized_end=1970
  _globals['_PREPAREPROVIDERCONFIG']._serialized_start=1973
  _globals['_PREPAREPROVIDERCONFIG']._serialized_end=2154
  _globals['_PREPAREPROVIDERCONFIG_REQUEST']._serialized_start=1998
  _globals['_PREPAREPROVIDERCONFIG_REQUEST']._serialized_end=2048
  _globals['_PREPAREPROVIDERCONFIG_RESPONSE']._serialized_start=2050
  _globals['_PREPAREPROVIDERCONFIG_RESPONSE']._serialized_end=2154
  _globals['_UPGRADERESOURCESTATE']._serialized_start=2157
  _globals['_UPGRADERESOURCESTATE']._serialized_end=2371
  _globals['_UPGRADERESOURCESTATE_REQUEST']._serialized_start=2181
  _globals['_UPGRADERESOURCESTATE_REQUEST']._serialized_end=2266
  _globals['_UPGRADERESOURCESTATE_RESPONSE']._serialized_start=2268
  _globals['_UPGRADERESOURCESTATE_RESPONSE']._serialized_end=2371
  _globals['_VALIDATERESOURCETYPECONFIG']._serialized_start=2374
  _globals['_VALIDATERESOURCETYPECONFIG']._serialized_end=2529
  _globals['_VALIDATERESOURCETYPECONFIG_REQUEST']._serialized_start=2404
  _globals['_VALIDATERESOURCETYPECONFIG_REQUEST']._serialized_end=2473
  _globals['_VALIDATERESOURCETYPECONFIG_RESPONSE']._serialized_start=2475
  _globals['_VALIDATERESOURCETYPECONFIG_RESPONSE']._serialized_end=2529
  _globals['_VALIDATEDATASOURCECONFIG']._serialized_start=2532
  _globals['_VALIDATEDATASOURCECONFIG']._serialized_end=2685
  _globals['_VALIDATEDATASOURCECONFIG_REQUEST']._serialized_start=2404
  _globals['_VALIDATEDATASOURCECONFIG_REQUEST']._serialized_end=2473
  _globals['_VALIDATEDATASOURCECONFIG_RESPONSE']._serialized_start=2475
  _globals['_VALIDATEDATASOURCECONFIG_RESPONSE']._serialized_end=2529
  _globals['_CONFIGURE']._serialized_start=2688
  _globals['_CONFIGURE']._serialized_end=2834
  _globals['_CONFIGURE_REQUEST']._serialized_start=2701
  _globals['_CONFIGURE_REQUEST']._serialized_end=2778
  _globals['_CONFIGURE_RESPONSE']._serialized_start=2475
  _globals['_CONFIGURE_RESPONSE']._serialized_end=2529
  _globals['_READRESOURCE']._serialized_start=2837
  _globals['_READRESOURCE']._serialized_end=3112
  _globals['_READRESOURCE_REQUEST']._serialized_start=2854
  _globals['_READRESOURCE_REQUEST']._serialized_end=2995
  _globals['_READRESOURCE_RESPONSE']._serialized_start=2997
  _globals['_READRESOURCE_RESPONSE']._serialized_end=3112
  _globals['_PLANRESOURCECHANGE']._serialized_start=3115
  _globals['_PLANRESOURCECHANGE']._serialized_end=3587
  _globals['_PLANRESOURCECHANGE_REQUEST']._serialized_start=3138
  _globals['_PLANRESOURCECHANGE_REQUEST']._serialized_end=3377
  _globals['_PLANRESOURCECHANGE_RESPONSE']._serialized_start=3380
  _globals['_PLANRESOURCECHANGE_RESPONSE']._serialized_end=3587
  _globals['_APPLYRESOURCECHANGE']._serialized_start=3590
  _globals['_APPLYRESOURCECHANGE']._serialized_end=3996
  _globals['_APPLYRESOURCECHANGE_REQUEST']._serialized_start=3614
  _globals['_APPLYRESOURCECHANGE_REQUEST']._serialized_end=3850
  _globals['_APPLYRESOURCECHANGE_RESPONSE']._serialized_start=3853
  _globals['_APPLYRESOURCECHANGE_RESPONSE']._serialized_end=3996
  _globals['_IMPORTRESOURCESTATE']._serialized_start=3999
  _globals['_IMPORTRESOURCESTATE']._serialized_end=4292
  _globals['_IMPORTRESOURCESTATE_REQUEST']._serialized_start=4022
  _globals['_IMPORTRESOURCESTATE_REQUEST']._serialized_end=4062
  _globals['_IMPORTRESOURCESTATE_IMPORTEDRESOURCE']._serialized_start=4064
  _globals['_IMPORTRESOURCESTATE_IMPORTEDRESOURCE']._serialized_end=4158
  _globals['_IMPORTRESOURCESTATE_RESPONSE']._serialized_start=4161
  _globals['_IMPORTRESOURCESTATE_RESPONSE']._serialized_end=4292
  _globals['_READDATASOURCE']._serialized_start=4295
  _globals['_READDATASOURCE']._serialized_end=4526
  _globals['_READDATASOURCE_REQUEST']._serialized_start=4313
  _globals['_READDATASOURCE_REQUEST']._serialized_end=4430
  _globals['_READDATASOURCE_RESPONSE']._serialized_start=4432
  _globals['_READDATASOURCE_RESPONSE']._serialized_end=4526
  _globals['_GETPROVISIONERSCHEMA']._serialized_start=4529
  _globals['_GETPROVISIONERSCHEMA']._serialized_end=4658
  _globals['_GETPROVISIONERSCHEMA_REQUEST']._serialized_start=446
  _globals['_GETPROVISIONERSCHEMA_REQUEST']._serialized_end=455
  _globals['_GETPROVISIONERSCHEMA_RESPONSE']._serialized_start=4564
  _globals['_GETPROVISIONERSCHEMA_RESPONSE']._serialized_end=4658
  _globals['_VALIDATEPROVISIONERCONFIG']._serialized_start=4661
  _globals['_VALIDATEPROVISIONERCONFIG']._serialized_end=4796
  _globals['_VALIDATEPROVISIONERCONFIG_REQUEST']._serialized_start=1998
  _globals['_VALIDATEPROVISIONERCONFIG_REQUEST']._serialized_end=2048
  _globals['_VALIDATEPROVISIONERCONFIG_RESPONSE']._serialized_start=2475
  _globals['_VALIDATEPROVISIONERCONFIG_RESPONSE']._serialized_end=2529
  _globals['_PROVISIONRESOURCE']._serialized_start=4799
  _globals['_PROVISIONRESOURCE']._serialized_end=4987
  _globals['_PROVISIONRESOURCE_REQUEST']._serialized_start=4820
  _globals['_PROVISIONRESOURCE_REQUEST']._serialized_end=4915
  _globals['_PROVISIONRESOURCE_RESPONSE']._serialized_start=4917
  _globals['_PROVISIONRESOURCE_RESPONSE']._serialized_end=4987
  _globals['_PROVIDER']._serialized_start=5029
  _globals['_PROVIDER']._serialized_end=6204
  _globals['_PROVISIONER']._serialized_start=6207
  _globals['_PROVISIONER']._serialized_end=6597
# @@protoc_insertion_point(module_scope)
