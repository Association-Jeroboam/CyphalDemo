// This is an AUTO-GENERATED UAVCAN DSDL data type implementation. Curious? See https://opencyphal.org.
// You shouldn't attempt to edit this file.
//
// Checking this file under version control is not recommended unless it is used as part of a high-SIL
// safety-critical codebase. The typical usage scenario is to generate it as part of the build process.
//
// To avoid conflicts with definitions given in the source DSDL file, all entities created by the code generator
// are named with an underscore at the end, like foo_bar_().
//
// Generator:     nunavut-1.8.0 (serialization was enabled)
// Source file:   /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/node/435.ExecuteCommand.1.0.dsdl
// Generated at:  2022-05-08 09:40:34.096738 UTC
// Is deprecated: yes
// Fixed port-ID: 435
// Full name:     uavcan.node.ExecuteCommand
// Version:       1.0
//
// Platform
//     python_implementation:  CPython
//     python_version:  3.10.4
//     python_release_level:  final
//     python_build:  ('main', 'Mar 31 2022 08:41:55')
//     python_compiler:  GCC 7.5.0
//     python_revision:
//     python_xoptions:  {}
//     runtime_platform:  Linux-5.4.0-109-generic-x86_64-with-glibc2.27
//
// Language Options
//     target_endianness:  little
//     omit_float_serialization_support:  False
//     enable_serialization_asserts:  False
//     enable_override_variable_array_capacity:  False
//     cast_format:  (({type}) {value})

//           _____  ______ _____  _____  ______ _____       _______ ______ _____
//          |  __ `|  ____|  __ `|  __ `|  ____/ ____|   /`|__   __|  ____|  __ `
//          | |  | | |__  | |__) | |__) | |__ | |       /  `  | |  | |__  | |  | |
//          | |  | |  __| |  ___/|  _  /|  __|| |      / /` ` | |  |  __| | |  | |
//          | |__| | |____| |    | | ` `| |___| |____ / ____ `| |  | |____| |__| |
//          |_____/|______|_|    |_|  `_`______`_____/_/    `_`_|  |______|_____/
//
// WARNING: this data type is deprecated and is nearing the end of its life cycle. Seek replacement.

#ifndef UAVCAN_NODE_EXECUTE_COMMAND_1_0_INCLUDED_
#define UAVCAN_NODE_EXECUTE_COMMAND_1_0_INCLUDED_

#include <nunavut/support/serialization.h>
#include <stdint.h>
#include <stdlib.h>

static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_TARGET_ENDIANNESS == 434322821,
              "/home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/node/435.ExecuteCommand.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_OMIT_FLOAT_SERIALIZATION_SUPPORT == 0,
              "/home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/node/435.ExecuteCommand.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_SERIALIZATION_ASSERTS == 0,
              "/home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/node/435.ExecuteCommand.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_OVERRIDE_VARIABLE_ARRAY_CAPACITY == 0,
              "/home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/node/435.ExecuteCommand.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_CAST_FORMAT == 2368206204,
              "/home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/node/435.ExecuteCommand.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );

#ifdef __cplusplus
extern "C" {
#endif

#define uavcan_node_ExecuteCommand_1_0_HAS_FIXED_PORT_ID_ true
#define uavcan_node_ExecuteCommand_1_0_FIXED_PORT_ID_     435U

#define uavcan_node_ExecuteCommand_1_0_FULL_NAME_             "uavcan.node.ExecuteCommand"
#define uavcan_node_ExecuteCommand_1_0_FULL_NAME_AND_VERSION_ "uavcan.node.ExecuteCommand.1.0"

#define uavcan_node_ExecuteCommand_Request_1_0_FULL_NAME_             "uavcan.node.ExecuteCommand.Request"
#define uavcan_node_ExecuteCommand_Request_1_0_FULL_NAME_AND_VERSION_ "uavcan.node.ExecuteCommand.Request.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define uavcan_node_ExecuteCommand_Request_1_0_EXTENT_BYTES_                    300UL
#define uavcan_node_ExecuteCommand_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 115UL
static_assert(uavcan_node_ExecuteCommand_Request_1_0_EXTENT_BYTES_ >= uavcan_node_ExecuteCommand_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

/// saturated uint16 COMMAND_RESTART = 65535
#define uavcan_node_ExecuteCommand_Request_1_0_COMMAND_RESTART (65535U)
/// saturated uint16 COMMAND_POWER_OFF = 65534
#define uavcan_node_ExecuteCommand_Request_1_0_COMMAND_POWER_OFF (65534U)
/// saturated uint16 COMMAND_BEGIN_SOFTWARE_UPDATE = 65533
#define uavcan_node_ExecuteCommand_Request_1_0_COMMAND_BEGIN_SOFTWARE_UPDATE (65533U)
/// saturated uint16 COMMAND_FACTORY_RESET = 65532
#define uavcan_node_ExecuteCommand_Request_1_0_COMMAND_FACTORY_RESET (65532U)
/// saturated uint16 COMMAND_EMERGENCY_STOP = 65531
#define uavcan_node_ExecuteCommand_Request_1_0_COMMAND_EMERGENCY_STOP (65531U)
/// saturated uint16 COMMAND_STORE_PERSISTENT_STATES = 65530
#define uavcan_node_ExecuteCommand_Request_1_0_COMMAND_STORE_PERSISTENT_STATES (65530U)

/// Array metadata for: saturated uint8[<=112] parameter
#define uavcan_node_ExecuteCommand_Request_1_0_parameter_ARRAY_CAPACITY_           112U
#define uavcan_node_ExecuteCommand_Request_1_0_parameter_ARRAY_IS_VARIABLE_LENGTH_ true

typedef struct
{
    /// saturated uint16 command
    uint16_t command;

    /// saturated uint8[<=112] parameter
    struct  /// Array address equivalence guarantee: &elements[0] == &parameter
    {
        uint8_t elements[uavcan_node_ExecuteCommand_Request_1_0_parameter_ARRAY_CAPACITY_];
        size_t count;
    } parameter;
} uavcan_node_ExecuteCommand_Request_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see uavcan_node_ExecuteCommand_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t uavcan_node_ExecuteCommand_Request_1_0_serialize_(
    const uavcan_node_ExecuteCommand_Request_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }


    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 920UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;





    {   // saturated uint16 command
        // Saturation code not emitted -- native representation matches the serialized representation.
        (void) memmove(&buffer[offset_bits / 8U], &obj->command, 2U);
        offset_bits += 16U;
    }




    {   // saturated uint8[<=112] parameter
        if (obj->parameter.count > 112)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint8
        buffer[offset_bits / 8U] = (uint8_t)(obj->parameter.count);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
        // Optimization prospect: this item is aligned at the byte boundary, so it is possible to use memmove().
        nunavutCopyBits(&buffer[0], offset_bits, obj->parameter.count * 8U, &obj->parameter.elements[0], 0U);
        offset_bits += obj->parameter.count * 8U;
    }


    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad0_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err0_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad0_);  // Optimize?
        if (_err0_ < 0)
        {
            return _err0_;
        }
        offset_bits += _pad0_;
    }
    // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.





    *inout_buffer_size_bytes = (size_t) (offset_bits / 8U);

    return NUNAVUT_SUCCESS;
}

/// Deserialize an instance from the provided buffer.
/// The lifetime of the resulting object is independent of the original buffer.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original buffer where possible.
///
/// @param obj      The object to update from the provided serialized representation.
///
/// @param buffer   The source buffer containing the serialized representation. There are no alignment requirements.
///                 If the buffer is shorter or longer than expected, it will be implicitly zero-extended or truncated,
///                 respectively; see Specification for "implicit zero extension" and "implicit truncation" rules.
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the supplied serialized
///                                 representation, in bytes. Upon return this value will be updated with the
///                                 size of the consumed fragment of the serialized representation (in bytes),
///                                 which may be smaller due to the implicit truncation rule, but it is guaranteed
///                                 to never exceed the original buffer size even if the implicit zero extension rule
///                                 was activated. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t uavcan_node_ExecuteCommand_Request_1_0_deserialize_(
    uavcan_node_ExecuteCommand_Request_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
{
    if ((out_obj == NULL) || (inout_buffer_size_bytes == NULL) || ((buffer == NULL) && (0 != *inout_buffer_size_bytes)))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    if (buffer == NULL)
    {
        buffer = (const uint8_t*)"";
    }


    const size_t capacity_bytes = *inout_buffer_size_bytes;
    const size_t capacity_bits = capacity_bytes * (size_t) 8U;
    size_t offset_bits = 0U;





    // saturated uint16 command
    out_obj->command = nunavutGetU16(&buffer[0], capacity_bytes, offset_bits, 16);
    offset_bits += 16U;




    // saturated uint8[<=112] parameter
    // Array length prefix: truncated uint8
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->parameter.count = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->parameter.count = 0U;
    }
    offset_bits += 8U;
    if (out_obj->parameter.count > 112U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    nunavutGetBits(&out_obj->parameter.elements[0], &buffer[0], capacity_bytes, offset_bits, out_obj->parameter.count * 8U);
    offset_bits += out_obj->parameter.count * 8U;


    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.

    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);


    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void uavcan_node_ExecuteCommand_Request_1_0_initialize_(uavcan_node_ExecuteCommand_Request_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = uavcan_node_ExecuteCommand_Request_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}



#define uavcan_node_ExecuteCommand_Response_1_0_FULL_NAME_             "uavcan.node.ExecuteCommand.Response"
#define uavcan_node_ExecuteCommand_Response_1_0_FULL_NAME_AND_VERSION_ "uavcan.node.ExecuteCommand.Response.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define uavcan_node_ExecuteCommand_Response_1_0_EXTENT_BYTES_                    48UL
#define uavcan_node_ExecuteCommand_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 1UL
static_assert(uavcan_node_ExecuteCommand_Response_1_0_EXTENT_BYTES_ >= uavcan_node_ExecuteCommand_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

/// saturated uint8 STATUS_SUCCESS = 0
#define uavcan_node_ExecuteCommand_Response_1_0_STATUS_SUCCESS (0U)
/// saturated uint8 STATUS_FAILURE = 1
#define uavcan_node_ExecuteCommand_Response_1_0_STATUS_FAILURE (1U)
/// saturated uint8 STATUS_NOT_AUTHORIZED = 2
#define uavcan_node_ExecuteCommand_Response_1_0_STATUS_NOT_AUTHORIZED (2U)
/// saturated uint8 STATUS_BAD_COMMAND = 3
#define uavcan_node_ExecuteCommand_Response_1_0_STATUS_BAD_COMMAND (3U)
/// saturated uint8 STATUS_BAD_PARAMETER = 4
#define uavcan_node_ExecuteCommand_Response_1_0_STATUS_BAD_PARAMETER (4U)
/// saturated uint8 STATUS_BAD_STATE = 5
#define uavcan_node_ExecuteCommand_Response_1_0_STATUS_BAD_STATE (5U)
/// saturated uint8 STATUS_INTERNAL_ERROR = 6
#define uavcan_node_ExecuteCommand_Response_1_0_STATUS_INTERNAL_ERROR (6U)

typedef struct
{
    /// saturated uint8 status
    uint8_t status;
} uavcan_node_ExecuteCommand_Response_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see uavcan_node_ExecuteCommand_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t uavcan_node_ExecuteCommand_Response_1_0_serialize_(
    const uavcan_node_ExecuteCommand_Response_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }


    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 8UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;





    {   // saturated uint8 status
        // Saturation code not emitted -- native representation matches the serialized representation.
        buffer[offset_bits / 8U] = (uint8_t)(obj->status);  // C std, 6.3.1.3 Signed and unsigned integers
        offset_bits += 8U;
    }


    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad1_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err1_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad1_);  // Optimize?
        if (_err1_ < 0)
        {
            return _err1_;
        }
        offset_bits += _pad1_;
    }
    // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.




    *inout_buffer_size_bytes = (size_t) (offset_bits / 8U);

    return NUNAVUT_SUCCESS;
}

/// Deserialize an instance from the provided buffer.
/// The lifetime of the resulting object is independent of the original buffer.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original buffer where possible.
///
/// @param obj      The object to update from the provided serialized representation.
///
/// @param buffer   The source buffer containing the serialized representation. There are no alignment requirements.
///                 If the buffer is shorter or longer than expected, it will be implicitly zero-extended or truncated,
///                 respectively; see Specification for "implicit zero extension" and "implicit truncation" rules.
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the supplied serialized
///                                 representation, in bytes. Upon return this value will be updated with the
///                                 size of the consumed fragment of the serialized representation (in bytes),
///                                 which may be smaller due to the implicit truncation rule, but it is guaranteed
///                                 to never exceed the original buffer size even if the implicit zero extension rule
///                                 was activated. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t uavcan_node_ExecuteCommand_Response_1_0_deserialize_(
    uavcan_node_ExecuteCommand_Response_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
{
    if ((out_obj == NULL) || (inout_buffer_size_bytes == NULL) || ((buffer == NULL) && (0 != *inout_buffer_size_bytes)))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    if (buffer == NULL)
    {
        buffer = (const uint8_t*)"";
    }


    const size_t capacity_bytes = *inout_buffer_size_bytes;
    const size_t capacity_bits = capacity_bytes * (size_t) 8U;
    size_t offset_bits = 0U;





    // saturated uint8 status
    if ((offset_bits + 8U) <= capacity_bits)
    {
        out_obj->status = buffer[offset_bits / 8U] & 255U;
    }
    else
    {
        out_obj->status = 0U;
    }
    offset_bits += 8U;


    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.

    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);


    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void uavcan_node_ExecuteCommand_Response_1_0_initialize_(uavcan_node_ExecuteCommand_Response_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = uavcan_node_ExecuteCommand_Response_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}



#ifdef __cplusplus
}
#endif
#endif // UAVCAN_NODE_EXECUTE_COMMAND_1_0_INCLUDED_
