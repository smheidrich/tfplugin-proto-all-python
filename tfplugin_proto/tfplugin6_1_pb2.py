# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tfplugin6_1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11tfplugin6_1.proto\x12\ttfplugin6\"-\n\x0c\x44ynamicValue\x12\x0f\n\x07msgpack\x18\x01 \x01(\x0c\x12\x0c\n\x04json\x18\x02 \x01(\x0c\"\xbd\x01\n\nDiagnostic\x12\x30\n\x08severity\x18\x01 \x01(\x0e\x32\x1e.tfplugin6.Diagnostic.Severity\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\x12+\n\tattribute\x18\x04 \x01(\x0b\x32\x18.tfplugin6.AttributePath\"/\n\x08Severity\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0b\n\x07WARNING\x10\x02\"\xa4\x01\n\rAttributePath\x12,\n\x05steps\x18\x01 \x03(\x0b\x32\x1d.tfplugin6.AttributePath.Step\x1a\x65\n\x04Step\x12\x18\n\x0e\x61ttribute_name\x18\x01 \x01(\tH\x00\x12\x1c\n\x12\x65lement_key_string\x18\x02 \x01(\tH\x00\x12\x19\n\x0f\x65lement_key_int\x18\x03 \x01(\x03H\x00\x42\n\n\x08selector\"4\n\x0cStopProvider\x1a\t\n\x07Request\x1a\x19\n\x08Response\x12\r\n\x05\x45rror\x18\x01 \x01(\t\"{\n\x08RawState\x12\x0c\n\x04json\x18\x01 \x01(\x0c\x12\x31\n\x07\x66latmap\x18\x02 \x03(\x0b\x32 .tfplugin6.RawState.FlatmapEntry\x1a.\n\x0c\x46latmapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf8\x07\n\x06Schema\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tfplugin6.Schema.Block\x1a\xd7\x01\n\x05\x42lock\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12/\n\nattributes\x18\x02 \x03(\x0b\x32\x1b.tfplugin6.Schema.Attribute\x12\x32\n\x0b\x62lock_types\x18\x03 \x03(\x0b\x32\x1d.tfplugin6.Schema.NestedBlock\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12/\n\x10\x64\x65scription_kind\x18\x05 \x01(\x0e\x32\x15.tfplugin6.StringKind\x12\x12\n\ndeprecated\x18\x06 \x01(\x08\x1a\xf9\x01\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x0c\x12-\n\x0bnested_type\x18\n \x01(\x0b\x32\x18.tfplugin6.Schema.Object\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08required\x18\x04 \x01(\x08\x12\x10\n\x08optional\x18\x05 \x01(\x08\x12\x10\n\x08\x63omputed\x18\x06 \x01(\x08\x12\x11\n\tsensitive\x18\x07 \x01(\x08\x12/\n\x10\x64\x65scription_kind\x18\x08 \x01(\x0e\x32\x15.tfplugin6.StringKind\x12\x12\n\ndeprecated\x18\t \x01(\x08\x1a\xf9\x01\n\x0bNestedBlock\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tfplugin6.Schema.Block\x12:\n\x07nesting\x18\x03 \x01(\x0e\x32).tfplugin6.Schema.NestedBlock.NestingMode\x12\x11\n\tmin_items\x18\x04 \x01(\x03\x12\x11\n\tmax_items\x18\x05 \x01(\x03\"M\n\x0bNestingMode\x12\x0b\n\x07INVALID\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\x08\n\x04LIST\x10\x02\x12\x07\n\x03SET\x10\x03\x12\x07\n\x03MAP\x10\x04\x12\t\n\x05GROUP\x10\x05\x1a\xe2\x01\n\x06Object\x12/\n\nattributes\x18\x01 \x03(\x0b\x32\x1b.tfplugin6.Schema.Attribute\x12\x35\n\x07nesting\x18\x03 \x01(\x0e\x32$.tfplugin6.Schema.Object.NestingMode\x12\x15\n\tmin_items\x18\x04 \x01(\x03\x42\x02\x18\x01\x12\x15\n\tmax_items\x18\x05 \x01(\x03\x42\x02\x18\x01\"B\n\x0bNestingMode\x12\x0b\n\x07INVALID\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\x08\n\x04LIST\x10\x02\x12\x07\n\x03SET\x10\x03\x12\x07\n\x03MAP\x10\x04\"\xef\x03\n\x11GetProviderSchema\x1a\t\n\x07Request\x1a\xce\x03\n\x08Response\x12#\n\x08provider\x18\x01 \x01(\x0b\x32\x11.tfplugin6.Schema\x12T\n\x10resource_schemas\x18\x02 \x03(\x0b\x32:.tfplugin6.GetProviderSchema.Response.ResourceSchemasEntry\x12Y\n\x13\x64\x61ta_source_schemas\x18\x03 \x03(\x0b\x32<.tfplugin6.GetProviderSchema.Response.DataSourceSchemasEntry\x12*\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\x12(\n\rprovider_meta\x18\x05 \x01(\x0b\x32\x11.tfplugin6.Schema\x1aI\n\x14ResourceSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.tfplugin6.Schema:\x02\x38\x01\x1aK\n\x16\x44\x61taSourceSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.tfplugin6.Schema:\x02\x38\x01\"\x84\x01\n\x16ValidateProviderConfig\x1a\x32\n\x07Request\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\"\xd6\x01\n\x14UpgradeResourceState\x1aU\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12&\n\traw_state\x18\x03 \x01(\x0b\x32\x13.tfplugin6.RawState\x1ag\n\x08Response\x12/\n\x0eupgraded_state\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\"\x97\x01\n\x16ValidateResourceConfig\x1a\x45\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\"\x9b\x01\n\x1aValidateDataResourceConfig\x1a\x45\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\"\x9a\x01\n\x11\x43onfigureProvider\x1aM\n\x07Request\x12\x19\n\x11terraform_version\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\"\x93\x02\n\x0cReadResource\x1a\x8d\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12.\n\rcurrent_state\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x12.\n\rprovider_meta\x18\x04 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1as\n\x08Response\x12*\n\tnew_state\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\x12\x0f\n\x07private\x18\x03 \x01(\x0c\"\xbc\x03\n\x12PlanResourceChange\x1a\xef\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12,\n\x0bprior_state\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x33\n\x12proposed_new_state\x18\x03 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\'\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x15\n\rprior_private\x18\x05 \x01(\x0c\x12.\n\rprovider_meta\x18\x06 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a\xb3\x01\n\x08Response\x12.\n\rplanned_state\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x32\n\x10requires_replace\x18\x02 \x03(\x0b\x32\x18.tfplugin6.AttributePath\x12\x17\n\x0fplanned_private\x18\x03 \x01(\x0c\x12*\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\"\xf9\x02\n\x13\x41pplyResourceChange\x1a\xec\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12,\n\x0bprior_state\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12.\n\rplanned_state\x18\x03 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\'\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x17\n\x0fplanned_private\x18\x05 \x01(\x0c\x12.\n\rprovider_meta\x18\x06 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1as\n\x08Response\x12*\n\tnew_state\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x0f\n\x07private\x18\x02 \x01(\x0c\x12*\n\x0b\x64iagnostics\x18\x03 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\"\xa5\x02\n\x13ImportResourceState\x1a(\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x1a^\n\x10ImportedResource\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12&\n\x05state\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x1a\x83\x01\n\x08Response\x12K\n\x12imported_resources\x18\x01 \x03(\x0b\x32/.tfplugin6.ImportResourceState.ImportedResource\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\"\xe7\x01\n\x0eReadDataSource\x1au\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12.\n\rprovider_meta\x18\x03 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a^\n\x08Response\x12&\n\x05state\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic*%\n\nStringKind\x12\t\n\x05PLAIN\x10\x00\x12\x0c\n\x08MARKDOWN\x10\x01\x32\xcc\t\n\x08Provider\x12`\n\x11GetProviderSchema\x12$.tfplugin6.GetProviderSchema.Request\x1a%.tfplugin6.GetProviderSchema.Response\x12o\n\x16ValidateProviderConfig\x12).tfplugin6.ValidateProviderConfig.Request\x1a*.tfplugin6.ValidateProviderConfig.Response\x12o\n\x16ValidateResourceConfig\x12).tfplugin6.ValidateResourceConfig.Request\x1a*.tfplugin6.ValidateResourceConfig.Response\x12{\n\x1aValidateDataResourceConfig\x12-.tfplugin6.ValidateDataResourceConfig.Request\x1a..tfplugin6.ValidateDataResourceConfig.Response\x12i\n\x14UpgradeResourceState\x12\'.tfplugin6.UpgradeResourceState.Request\x1a(.tfplugin6.UpgradeResourceState.Response\x12`\n\x11\x43onfigureProvider\x12$.tfplugin6.ConfigureProvider.Request\x1a%.tfplugin6.ConfigureProvider.Response\x12Q\n\x0cReadResource\x12\x1f.tfplugin6.ReadResource.Request\x1a .tfplugin6.ReadResource.Response\x12\x63\n\x12PlanResourceChange\x12%.tfplugin6.PlanResourceChange.Request\x1a&.tfplugin6.PlanResourceChange.Response\x12\x66\n\x13\x41pplyResourceChange\x12&.tfplugin6.ApplyResourceChange.Request\x1a\'.tfplugin6.ApplyResourceChange.Response\x12\x66\n\x13ImportResourceState\x12&.tfplugin6.ImportResourceState.Request\x1a\'.tfplugin6.ImportResourceState.Response\x12W\n\x0eReadDataSource\x12!.tfplugin6.ReadDataSource.Request\x1a\".tfplugin6.ReadDataSource.Response\x12Q\n\x0cStopProvider\x12\x1f.tfplugin6.StopProvider.Request\x1a .tfplugin6.StopProvider.ResponseB3Z1github.com/hashicorp/terraform/internal/tfplugin6b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tfplugin6_1_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/hashicorp/terraform/internal/tfplugin6'
  _RAWSTATE_FLATMAPENTRY._options = None
  _RAWSTATE_FLATMAPENTRY._serialized_options = b'8\001'
  _SCHEMA_OBJECT.fields_by_name['min_items']._options = None
  _SCHEMA_OBJECT.fields_by_name['min_items']._serialized_options = b'\030\001'
  _SCHEMA_OBJECT.fields_by_name['max_items']._options = None
  _SCHEMA_OBJECT.fields_by_name['max_items']._serialized_options = b'\030\001'
  _GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY._options = None
  _GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY._serialized_options = b'8\001'
  _GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY._options = None
  _GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY._serialized_options = b'8\001'
  _globals['_STRINGKIND']._serialized_start=4590
  _globals['_STRINGKIND']._serialized_end=4627
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
  _globals['_STOPPROVIDER']._serialized_start=438
  _globals['_STOPPROVIDER']._serialized_end=490
  _globals['_STOPPROVIDER_REQUEST']._serialized_start=454
  _globals['_STOPPROVIDER_REQUEST']._serialized_end=463
  _globals['_STOPPROVIDER_RESPONSE']._serialized_start=465
  _globals['_STOPPROVIDER_RESPONSE']._serialized_end=490
  _globals['_RAWSTATE']._serialized_start=492
  _globals['_RAWSTATE']._serialized_end=615
  _globals['_RAWSTATE_FLATMAPENTRY']._serialized_start=569
  _globals['_RAWSTATE_FLATMAPENTRY']._serialized_end=615
  _globals['_SCHEMA']._serialized_start=618
  _globals['_SCHEMA']._serialized_end=1634
  _globals['_SCHEMA_BLOCK']._serialized_start=686
  _globals['_SCHEMA_BLOCK']._serialized_end=901
  _globals['_SCHEMA_ATTRIBUTE']._serialized_start=904
  _globals['_SCHEMA_ATTRIBUTE']._serialized_end=1153
  _globals['_SCHEMA_NESTEDBLOCK']._serialized_start=1156
  _globals['_SCHEMA_NESTEDBLOCK']._serialized_end=1405
  _globals['_SCHEMA_NESTEDBLOCK_NESTINGMODE']._serialized_start=1328
  _globals['_SCHEMA_NESTEDBLOCK_NESTINGMODE']._serialized_end=1405
  _globals['_SCHEMA_OBJECT']._serialized_start=1408
  _globals['_SCHEMA_OBJECT']._serialized_end=1634
  _globals['_SCHEMA_OBJECT_NESTINGMODE']._serialized_start=1328
  _globals['_SCHEMA_OBJECT_NESTINGMODE']._serialized_end=1394
  _globals['_GETPROVIDERSCHEMA']._serialized_start=1637
  _globals['_GETPROVIDERSCHEMA']._serialized_end=2132
  _globals['_GETPROVIDERSCHEMA_REQUEST']._serialized_start=454
  _globals['_GETPROVIDERSCHEMA_REQUEST']._serialized_end=463
  _globals['_GETPROVIDERSCHEMA_RESPONSE']._serialized_start=1670
  _globals['_GETPROVIDERSCHEMA_RESPONSE']._serialized_end=2132
  _globals['_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY']._serialized_start=1982
  _globals['_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY']._serialized_end=2055
  _globals['_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY']._serialized_start=2057
  _globals['_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY']._serialized_end=2132
  _globals['_VALIDATEPROVIDERCONFIG']._serialized_start=2135
  _globals['_VALIDATEPROVIDERCONFIG']._serialized_end=2267
  _globals['_VALIDATEPROVIDERCONFIG_REQUEST']._serialized_start=2161
  _globals['_VALIDATEPROVIDERCONFIG_REQUEST']._serialized_end=2211
  _globals['_VALIDATEPROVIDERCONFIG_RESPONSE']._serialized_start=2213
  _globals['_VALIDATEPROVIDERCONFIG_RESPONSE']._serialized_end=2267
  _globals['_UPGRADERESOURCESTATE']._serialized_start=2270
  _globals['_UPGRADERESOURCESTATE']._serialized_end=2484
  _globals['_UPGRADERESOURCESTATE_REQUEST']._serialized_start=2294
  _globals['_UPGRADERESOURCESTATE_REQUEST']._serialized_end=2379
  _globals['_UPGRADERESOURCESTATE_RESPONSE']._serialized_start=2381
  _globals['_UPGRADERESOURCESTATE_RESPONSE']._serialized_end=2484
  _globals['_VALIDATERESOURCECONFIG']._serialized_start=2487
  _globals['_VALIDATERESOURCECONFIG']._serialized_end=2638
  _globals['_VALIDATERESOURCECONFIG_REQUEST']._serialized_start=2513
  _globals['_VALIDATERESOURCECONFIG_REQUEST']._serialized_end=2582
  _globals['_VALIDATERESOURCECONFIG_RESPONSE']._serialized_start=2584
  _globals['_VALIDATERESOURCECONFIG_RESPONSE']._serialized_end=2638
  _globals['_VALIDATEDATARESOURCECONFIG']._serialized_start=2641
  _globals['_VALIDATEDATARESOURCECONFIG']._serialized_end=2796
  _globals['_VALIDATEDATARESOURCECONFIG_REQUEST']._serialized_start=2513
  _globals['_VALIDATEDATARESOURCECONFIG_REQUEST']._serialized_end=2582
  _globals['_VALIDATEDATARESOURCECONFIG_RESPONSE']._serialized_start=2584
  _globals['_VALIDATEDATARESOURCECONFIG_RESPONSE']._serialized_end=2638
  _globals['_CONFIGUREPROVIDER']._serialized_start=2799
  _globals['_CONFIGUREPROVIDER']._serialized_end=2953
  _globals['_CONFIGUREPROVIDER_REQUEST']._serialized_start=2820
  _globals['_CONFIGUREPROVIDER_REQUEST']._serialized_end=2897
  _globals['_CONFIGUREPROVIDER_RESPONSE']._serialized_start=2584
  _globals['_CONFIGUREPROVIDER_RESPONSE']._serialized_end=2638
  _globals['_READRESOURCE']._serialized_start=2956
  _globals['_READRESOURCE']._serialized_end=3231
  _globals['_READRESOURCE_REQUEST']._serialized_start=2973
  _globals['_READRESOURCE_REQUEST']._serialized_end=3114
  _globals['_READRESOURCE_RESPONSE']._serialized_start=3116
  _globals['_READRESOURCE_RESPONSE']._serialized_end=3231
  _globals['_PLANRESOURCECHANGE']._serialized_start=3234
  _globals['_PLANRESOURCECHANGE']._serialized_end=3678
  _globals['_PLANRESOURCECHANGE_REQUEST']._serialized_start=3257
  _globals['_PLANRESOURCECHANGE_REQUEST']._serialized_end=3496
  _globals['_PLANRESOURCECHANGE_RESPONSE']._serialized_start=3499
  _globals['_PLANRESOURCECHANGE_RESPONSE']._serialized_end=3678
  _globals['_APPLYRESOURCECHANGE']._serialized_start=3681
  _globals['_APPLYRESOURCECHANGE']._serialized_end=4058
  _globals['_APPLYRESOURCECHANGE_REQUEST']._serialized_start=3705
  _globals['_APPLYRESOURCECHANGE_REQUEST']._serialized_end=3941
  _globals['_APPLYRESOURCECHANGE_RESPONSE']._serialized_start=3943
  _globals['_APPLYRESOURCECHANGE_RESPONSE']._serialized_end=4058
  _globals['_IMPORTRESOURCESTATE']._serialized_start=4061
  _globals['_IMPORTRESOURCESTATE']._serialized_end=4354
  _globals['_IMPORTRESOURCESTATE_REQUEST']._serialized_start=4084
  _globals['_IMPORTRESOURCESTATE_REQUEST']._serialized_end=4124
  _globals['_IMPORTRESOURCESTATE_IMPORTEDRESOURCE']._serialized_start=4126
  _globals['_IMPORTRESOURCESTATE_IMPORTEDRESOURCE']._serialized_end=4220
  _globals['_IMPORTRESOURCESTATE_RESPONSE']._serialized_start=4223
  _globals['_IMPORTRESOURCESTATE_RESPONSE']._serialized_end=4354
  _globals['_READDATASOURCE']._serialized_start=4357
  _globals['_READDATASOURCE']._serialized_end=4588
  _globals['_READDATASOURCE_REQUEST']._serialized_start=4375
  _globals['_READDATASOURCE_REQUEST']._serialized_end=4492
  _globals['_READDATASOURCE_RESPONSE']._serialized_start=4494
  _globals['_READDATASOURCE_RESPONSE']._serialized_end=4588
  _globals['_PROVIDER']._serialized_start=4630
  _globals['_PROVIDER']._serialized_end=5858
# @@protoc_insertion_point(module_scope)