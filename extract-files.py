#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/amazon/mt8169-common',
    'device/amazon/tungsten',
    'hardware/amazon',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'vendor/amazon/mt8169-common',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    ('vendor/lib/hw/audio.primary.mt8169.so', 'vendor/lib/hw/fireos.hardware.audio@6.0-impl.so',
     'vendor/lib/libasp.so', 'vendor/lib/libaudioprimarydevicehalifclient.so', 'vendor/lib/libedgeflow_core.so',
     'vendor/lib/libtensorflowlite_c-v30.so'): blob_fixup()
        .replace_needed('android.hardware.audio.common-util.so', 'android.hardware.audio.common-util-v30.so')
        .replace_needed('android.hardware.audio.common@6.0-util.so', 'android.hardware.audio.common@6.0-util-v30.so')
        .replace_needed('libmedia_helper.so', 'libmedia_helper-v30.so')
        .replace_needed('libtensorflowlite_c.so', 'libtensorflowlite_c-v30.so'),
    'vendor/lib/libMtkOmxVenc.so': blob_fixup()
        .replace_needed('libui.so', 'libui-v30.so'),
    'vendor/lib/libwvhidl.so': blob_fixup()
        .add_needed('libcrypto_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'tungsten',
    'amazon',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'mt8169-common', module.vendor)
    utils.run()
