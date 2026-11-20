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
    'vendor/bin/hw/camerahalserver': blob_fixup()
        .remove_needed('libudf.so')
        .add_needed('libaemgr_shim.so'),
    ('vendor/lib/hw/audio.primary.mt8169.so', 'vendor/lib/libasp.so',
     'vendor/lib/libaudioprimarydevicehalifclient.so', 'vendor/lib/libedgeflow_core.so',
     'vendor/lib/libtensorflowlite_c-v30.so'): blob_fixup()
        .replace_needed('android.hardware.audio.common-util.so', 'android.hardware.audio.common-util-v30.so')
        .replace_needed('android.hardware.audio.common@6.0-util.so', 'android.hardware.audio.common@6.0-util-v30.so')
        .replace_needed('libmedia_helper.so', 'libmedia_helper-v30.so')
        .replace_needed('libtensorflowlite_c.so', 'libtensorflowlite_c-v30.so'),
    'vendor/lib/hw/fireos.hardware.audio@6.0-impl.so': blob_fixup()
        .replace_needed('android.hardware.audio.common-util.so', 'android.hardware.audio.common-util-v30.so')
        .replace_needed('android.hardware.audio.common@6.0-util.so', 'android.hardware.audio.common@6.0-util-v30.so')
        .replace_needed('libmedia_helper.so', 'libmedia_helper-v30.so')
        .replace_needed('libutils.so', 'libutils-v32.so'),
    'vendor/lib/libMtkOmxVenc.so': blob_fixup()
        .replace_needed('libui.so', 'libui-v30.so'),
    'vendor/lib/libwvhidl.so': blob_fixup()
        .add_needed('libcrypto_shim.so'),
    'vendor/lib64/hw/android.hardware.camera.provider@2.6-impl-mediatek.so': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
    'vendor/lib64/libcam.halisp.so': blob_fixup()
        .sig_replace('00 20 80 52 37 20 00 94 fc 03 00 aa', '00 a6 81 52'),
    'vendor/lib64/libcam.isptuning.so': blob_fixup()
        .sig_replace('00 20 80 52 d6 06 02 94 fc 03 00 aa', '00 a6 81 52'),
    'vendor/lib64/libmtkcam_device3_app.so': blob_fixup()
        .remove_needed('android.frameworks.displayservice@1.0.so')
        .remove_needed('android.hardware.graphics.common-V1-ndk_platform.so')
        .replace_needed('libutils.so', 'libutils-v32.so'),
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
