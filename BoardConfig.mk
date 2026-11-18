#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/amazon/tungsten

# Inherit from the common tree
include device/amazon/mt8169-common/BoardConfigCommon.mk

# Partitions
BOARD_SUPER_PARTITION_SIZE := 4078960640

# Partitions (Dynamic)
BOARD_MAIN_SIZE := 4076863488

# Verified Boot
BOARD_AVB_ROLLBACK_INDEX := 2
BOARD_AVB_BOOT_ROLLBACK_INDEX := 7
BOARD_AVB_RECOVERY_ROLLBACK_INDEX := 7

# Inherit the proprietary files
include vendor/amazon/tungsten/BoardConfigVendor.mk
