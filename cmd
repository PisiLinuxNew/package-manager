#!/bin/sh

#   $$ -> pid
#   $# -> argüman sayısı
#   $* -> argümanlar

if [ $# == 0 ]; then
    echo "Kullnım:"
    echo "========"
    echo "      $0 [opt]"
    echo "opt:"
    echo "____"
    echo "  b : build"
    echo "  bi: build and install"
    echo "  c : clean (yetki ister)"
    echo "  i : install (yetki ister)"
    echo "  r : run"
    echo "  u : uninstall (yetki ister)"
    exit
fi

if [ $1 == 'b' ]; then
    echo "derleme başlatıldı."
    python setup.py build
    echo "derleme bitti."
elif [ $1 == 'i' ]; then
    echo "yükleme işlemi başlatıldı."
    sudo python setup.py install
    echo "yükleme işlemi bitti."
elif [ $1 == 'bi' ]; then
    echo "işlem başlatıldı."
    python setup.py build
    sudo python setup.py install
    echo "yükleme işlemi bitti."
elif [ $1 == 'c' ]; then
    echo "temizleme işlemi başlatıldı."
    sudo python setup.py clean
    echo "temizleme işlemi bitti."
elif [ $1 == 'r' ]; then
    echo "program çalıştırılıyor"
    python build/main.py
elif [ $1 == 'rt' ]; then
    echo "program çalıştırılıyor"
    python build/main.py tray
elif [ $1 == 're' ]; then
    echo "release messages"
    lrelease-qt5 lang/*.ts
elif [ $1 == 'u' ]; then
    echo "kaldırma işlemi başlatıldı."
    sudo python setup.py uninstall
    echo "kaldırma işlemi bitti."
elif [ $1 == 'up' ]; then
    echo "program çalıştırılıyor"
    python setup.py update_messages
else
    echo -e "\e[1;31margüman geçerli değil.\e[0m"
    echo "Kullnım:"
    echo "========"
    echo "      $0 [opt]"
    echo "opt:"
    echo "____"
    echo "  b : build"
    echo "  bi: build and install"
    echo "  c : clean (yetki ister)"
    echo "  i : install (yetki ister)"
    echo "  r : run"
    echo "  re: release messages"
    echo "  u : uninstall (yetki ister)"
    echo "  up: update messages"
fi
